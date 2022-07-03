import logging


Log_Format = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename = "lodfile.log",
                    filemode = "w",
                    format = Log_Format,
                    level = logging.ERROR)

logger = logging.getLogger()
e="Server failed to authenticate the request. Make sure the value of Authorization header is formed correctly including the signature.<?xml version='1.0' encoding='utf-8'?><Error><Code>AuthenticationFailed</Code><Message>Server failed to authenticate the request.Make sure the value of Authorization header is formed correctly including the signature.RequestId:dc7a100d-701e-000b-4b8c-66f6ec000000 Time:2022-05-13T05:40:54.8337386Z</Message><AuthenticationErrorDetail>The MAC signature found in the HTTP request 'ywfdlhMt/as5c+mMKwkvCPklG+UItPZMM0QdzEaCmCE=' is not the same as any computed signature.Server used following string to sign: 'PUT 2155 x-ms-blob-type:BlockBlob x-ms-client-request-id:4314a0d3-d27f-11ec-96f2-f69ec890e06b x-ms-date:Fri, 13 May 2022 05:40:56 GMT x-ms-version:2017-04-17 /setuptest1906/testcontainer/Squirrel-CheckForUpdate.log'.</AuthenticationErrorDetail></Error>"
#es=e.split('.')
#print(es[0]+', '+ es[1])
logger.error(e)