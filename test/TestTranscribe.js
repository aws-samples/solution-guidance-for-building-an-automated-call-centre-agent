
const transcriptionUtils = require('../src/utils/TranscriptionUtils');

process.env.TRANSCRIPTS_TABLE = `${process.env.stage}-${process.env.service}-transcripts`;

transcriptionUtils.transcribeStream('arn:aws:kinesisvideo:ap-southeast-2:192372509350:stream/live-voice-connect-wwso-llm-dev-contact-45753de2-5ab0-475f-b1f3-97e6a8ea0cd7/1701219179060',
  '91343852333181457151482848367510221787863225613', '346a5fc9-965d-4283-b500-2e05f8dd2fe1', process.env.whisperEndPoint);
