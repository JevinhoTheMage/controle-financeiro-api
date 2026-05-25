from pydantic import BaseModel, Field
from typing import Optional
from datetime import date


class ConfigIn(BaseModel):
    salario: float = Field(..., gt=0)
    percentual_investimento: float = Field(..., ge=0, le=100)


class GastoFixoIn(BaseModel):
    descricao: str
    valor: float = Field(..., gt=0)
    vencimento_dia: int = Field(..., ge=1, le=31)


class GastoDiarioIn(BaseModel):
    data: date
    descricao: str
    categoria: str
    valor: float = Field(..., gt=0)
    forma_pagamento: str
    mes_referencia: Optional[str] = None


class InvestimentoIn(BaseModel):
    mes_referencia: str
    valor_aportado: float = Field(..., gt=0)
    rendimento_percentual: float = Field(0.8)
