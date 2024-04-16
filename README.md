# Amazon Connect Real Time Transcription using Whisper in the IVR

## Installation

Customise env/dev.sh with your target region, account number and whisper end point. Pay attention to the AWS Profile name, if deploying and testing from the command line.

Change the stage and rename to env/<stage>.sh to deploy to a new stage environment.

Execute this script once:

    ./scripts/create_deployment_bucket.sh <stage>

To deploy execute this script as often as required:

    ./scripts/serverless_deploy.sh <stage>

Set up a contact flow that starts media streaming and passes the following parameters to the ProcessStream Lambda:

    kvsStreamArn: the stream arn from the contact attribute in Connect
    kvsStartFragment: the kvs start fragment number from the contact attribute in Connect

You need to add any lambda functions used to the Amazon Connect instance

ContactId is fetched from the standard request attribute (you may prefer initial contact id):

    event.Details.ContactData.ContactId

This should start populating an IVR real time transcript into DynamoDB.

Enable KVS media streaming in your Connect instance and set a sane retention period for (KVS 24 hours minimum during testing)

## Testing

You may modify the test/TestTranscribe.js file for console based testing, update the KVS stream arn, start fragment number and contact id.

    source ./env/dev.sh && node ./test/TestTranscribe.js

Outputs to the console and writes to DynamoDB:

    Made transcript: {
      "contactId": "346a5fc9-965d-4283-b500-2e05f8dd2fe1",
      "transcriptId": "890b9df9-9dd3-4b0e-b4be-6ec9a5b9f293",
      "channel": "VOICE",
      "content": "Please tell me in a few words how I can help you today.",
      "participant": "AGENT",
      "startOffset": 1279,
      "endOffset": 4736
    }
    Made transcript: {
      "contactId": "346a5fc9-965d-4283-b500-2e05f8dd2fe1",
      "transcriptId": "f294614e-6649-4add-b62c-f01d78359090",
      "channel": "VOICE",
      "content": "I'd like to get help with my insurance.",
      "participant": "CUSTOMER",
      "startOffset": 5183,
      "endOffset": 9471
    }

    ...

Commented out code in src/utils/TranscriptionUtils.js allows dumping of raw audio for import via Audacity:

    File / Import / Raw data ...

Raw data import dialog settings for a track:

    Encoding: Signed 16-bit PCM
    Byte order: Little Endian (or default on mac)
    Channels: 1 channel mono
    Amount: 100%
    Sample rate: 8000

## Authors

Authors are cpro@amazon.com and jospas@amazon.com
