import pandas as pd
from fastapi import FastAPI
from schemas import HousePrice, HousePriceResponse
import uvicorn

app = FastAPI()


@app.get('/')
def index():
    return {"detail": "please make a post request to /predict"}


@app.post('/predict/')
def predict(request: HousePrice):
    #data = dict(request)



    POSTED_BY_Dealer = request.POSTED_BY
    if(POSTED_BY_Dealer == 'Dealer'):
        POSTED_BY_Dealer = 1
        POSTED_BY_Owner = 0
    elif(POSTED_BY_Dealer == 'Owner'):
        POSTED_BY_Dealer = 0
        POSTED_BY_Owner = 1
    else:
        POSTED_BY_Dealer = 0
        POSTED_BY_Owner = 0


    UNDER_CONSTRUCTION = request.UNDER_CONSTRUCTION
    RERA = request.RERA
    BHK_NO = request.BHK_NO

    BHK_OR_RK_RK = request.BHK_OR_RK
    if(BHK_OR_RK_RK == 'BHK'):
        BHK_OR_RK_RK = 0
    else:
        BHK_OR_RK_RK = 1

    SQUARE_FT = request.SQUARE_FT
    READY_TO_MOVE = request.READY_TO_MOVE
    RESALE = request.RESALE

    LONGITUDE = request.LONGITUDE
    LATITUDE = request.LATITUDE

    data = {"POSTED_BY_Dealer" : POSTED_BY_Dealer, "POSTED_BY_Owner" : POSTED_BY_Owner, "UNDER_CONSTRUCTION" : UNDER_CONSTRUCTION,
            "RERA" : RERA,  "BHK_NO" :  BHK_NO, "BHK_OR_RK_RK" : BHK_OR_RK_RK,
            "SQUARE_FT" : SQUARE_FT, "READY_TO_MOVE" : READY_TO_MOVE, "RESALE" : RESALE, "LONGITUDE" : LONGITUDE, "LATITUDE" : LATITUDE}



    scale = pd.read_pickle('Model/scale.pkl')


    #with open("Model/scale.pkl", "rb") as gh:
        #scale = pickle.load(gh)


    temp = []
    columns = ["UNDER_CONSTRUCTION", "RERA","BHK_NO","SQUARE_FT","READY_TO_MOVE",
               "RESALE","LONGITUDE","LATITUDE",
               "POSTED_BY_Dealer","POSTED_BY_Owner","BHK_OR_RK_RK"]
    for i in columns:
        temp.append(data[i])
    x = [temp]
    new_data = scale.transform(x)
    # print(new_data)

    UNDER_CONSTRUCTION = new_data[0][0]
    RERA= new_data[0][1]
    BHK_NO = new_data[0][2]
    SQUARE_FT = new_data[0][3]
    READY_TO_MOVE = new_data[0][4]
    RESALE = new_data[0][5]
    LONGITUDE = new_data[0][6]
    LATITUDE = new_data[0][7]
    POSTED_BY_Dealer = new_data[0][8]
    POSTED_BY_Owner = new_data[0][9]
    BHK_OR_RK_RK = new_data[0][10]

    model = pd.read_pickle('Model/model.pkl')
    #with open("Model/model.pkl", "rb") as fh:
        #model = pickle.load(fh)


    Outcome = model.predict(
        [[UNDER_CONSTRUCTION,RERA,BHK_NO,SQUARE_FT,READY_TO_MOVE,
               RESALE,LONGITUDE,LATITUDE,
               POSTED_BY_Dealer,POSTED_BY_Owner,BHK_OR_RK_RK]])
        
    Result = (Outcome[0])

    # print(classification)
    data['Outcome'] = Result
    return data
    # return data


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000)

#uvicorn main:app --reload

