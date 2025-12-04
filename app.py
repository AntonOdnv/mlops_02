from fastapi import Body, Depends, FastAPI, Header
from typing import Annotated, List, Dict, Any
from pydantic import BaseModel, validator
import uvicorn
import joblib
from fastapi import HTTPException 
from typing import List, Dict     
import pandas as pd                

app = FastAPI()

# query
# path
# header
# body 

@app.get('/simple')
def simple():
    return "Hello!!!"

# @app.get('/test')
# def test(name: str):
#     return f"Hello, {name}!!!"

# @app.get('/test/{name}')
# def test(name: str):
#     return f"Hello, {name}!!!"

# @app.get('/test')
# def test(name: Annotated[str, Header(alias="X-Name")]) -> str: 
#     return f"Hello, {name}!!!"

# @app.post('/test')
# def test(name: Annotated[str, Body()]) -> str: 
#     return f"Hello, {name}!!!"

# class MLRequest(BaseModel):
#     a: float
#     b: float

# class MLResponse(BaseModel):
#     answer: float

# class ML_df_Response(BaseModel):
#     answer: List[float]

# # Модель для прямого DataFrame JSON
# class ML_df_Request(BaseModel):
#     data: Dict[str, List[float]]  # {"data": {"col1": [1,2,3], "col2": [4,5,6]}}
    
#     @validator('data')
#     def validate_columns(cls, v):
#         if len(v) != 2:
#             raise ValueError('Должно быть ровно 2 колонки')
        
#         # Проверяем что все колонки имеют одинаковую длину
#         col_lengths = [len(values) for values in v.values()]
#         if len(set(col_lengths)) != 1:
#             raise ValueError('Все колонки должны иметь одинаковую длину')
            
#         return v
    
#     def to_dataframe(self) -> pd.DataFrame:
#         return pd.DataFrame(self.data)


# loaded_model = None


# def load_model():
#     global loaded_model
#     if loaded_model is None:
#         loaded_model = joblib.load('model.joblib')
#     return loaded_model

# @app.post('/predict')
# def predict(data: Annotated[MLRequest, Body()], model=Depends(load_model)) -> MLResponse:
#     prediction = model.predict([[data.a, data.b]])
#     return MLResponse(answer=prediction[0])
    
    
# @app.post('/batch_json')
# def batch_json(data: Annotated[List[MLRequest], Body()], model=Depends(load_model)) -> ML_df_Response:
   
#     # Восстанавливаем DataFrame из JSON
#     df = pd.DataFrame(
#         {
#             'a': [x.a for x in data],
#             'b': [x.b for x in data]
#         }
#     )
#     predictions = model.predict(df)
#     return ML_df_Response(answer=predictions)


# @app.post('/batch_predict')
# def batch_predict(data: Annotated[ML_df_Request, Body()], model=Depends(load_model)) -> ML_df_Response:
    
#     try:
#         # Восстанавливаем DataFrame из JSON
#         df = data.to_dataframe()
        
#         # Проверяем что все значения числовые
#         if not all(df[col].dtype.kind in 'ifc' for col in df.columns):
#             raise ValueError("Все значения должны быть числовыми")
        
#         # Вычисляем предсказания
#         features = df.values
#         predictions = model.predict(features)
        
#         return ML_df_Response(answer=predictions.tolist())
        
#     except Exception as e:
#         raise HTTPException(500, f"Ошибка обработки DataFrame: {str(e)}")


def main():
    uvicorn.run(app, host="0.0.0.0")

if __name__ == '__main__':
    main()
