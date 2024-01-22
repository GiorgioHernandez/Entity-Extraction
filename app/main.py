import time 
import logging
from fastapi import FastAPI, UploadFile, File, HTTPException
from app.inference import Process

logger = logging.getLogger("mylogger")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

app = FastAPI()

process = Process()

@app.post('/api/extraction')
async def extraction(
    file: UploadFile = File(..., description='pdf or image file'), 
): 
    t0 = time.time()
    filename = file.filename
    logger.info(f'Processing ... {filename}')

    try: 
        text = await process.data_unstructured(file=file)
        response, cost = await process.inference(text=text)

        out = {
            'filename':filename,
            'process_time(seconds)':round(time.time()-t0,2),
            'cost(USD)': cost,
            'Fields': response
        }
        logger.info(f'Successed process!')
        return out

    except Exception as err:
        logger.debug(f'No procesable: {err}')
        raise HTTPException(status_code=400, detail=f'No procesable: {err}')


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8080)