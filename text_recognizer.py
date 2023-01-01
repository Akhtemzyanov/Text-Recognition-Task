# Модель в Pytorch для распознавания текста на картинке 

import torch
import torch.nn as nn

# Класс, в котором будет происходить инициализация модели, обучение и прогнозирование
class TextRecognizer:
  
  # Задаём параметры обучения
  def __init__(self, epochs = 1):
    
    self.epochs = epochs
    self.model = nn.Sequential(

    )
    self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    self.model.to(self.device)

