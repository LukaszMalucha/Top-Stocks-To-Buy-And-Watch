import yfinance as yf
from core.models import CompanyModel, UpdateModel
from datetime import datetime
import numpy as np
from django.utils import timezone
from analytics import sectors


def update_done():
    UpdateModel.objects.create()


def dataset_creator(dataset, ratio, asc=False):
    dataset = dataset[["shortName", "symbol", ratio]]
    dataset = dataset[dataset[ratio] != np.nan]
    dataset = dataset.dropna()
    dataset["value"] = dataset[ratio]
    dataset = dataset.drop([ratio], axis=1)
    if asc:
        dataset.sort_values(['value'], inplace=True, ascending=False)
    else:
        dataset.sort_values(['value'], inplace=True)
    dataset = dataset[dataset['value'] > 0]
    dataset = dataset.head(10)
    dataset["shortName"] = dataset["shortName"].apply(
        lambda x: x[:24] + "." if len(x) > 20 else x)
    dataset["shortName"] = dataset["shortName"].str.replace("\.\.", ".")
    dataset = dataset.to_dict("records")

    return dataset


def upload(stocks, sector):
    for stock in stocks:
        if CompanyModel.objects.filter(symbol=stock).exists():
            info = yf.Ticker(stock).info
            updated_company = CompanyModel.objects.get(symbol=stock)
            updated_company.shortName = info.get('shortName')
            updated_company.symbol = info.get('symbol')
            updated_company.dividendRate = info.get("dividendRate")
            updated_company.trailingPE = info.get("trailingPE")
            updated_company.forwardPE = info.get("forwardPE")
            updated_company.dividendYield = info.get("dividendYield")
            updated_company.enterpriseToRevenue = info.get("enterpriseToRevenue")
            updated_company.enterpriseToEbitda = info.get("enterpriseToEbitda")
            updated_company.pegRatio = info.get("pegRatio")
            updated_company.trailingEps = info.get("trailingEps")
            updated_company.forwardEps = info.get("forwardEps")
            updated_company.updated = timezone.now()
            updated_company.sector = sector
            updated_company.save()

        else:
            try:
                info = yf.Ticker(stock).info
                company = CompanyModel.objects.create(
                    shortName=info.get('shortName'),
                    symbol=info.get('symbol'),
                    dividendRate=info.get("dividendRate"),
                    trailingPE=info.get("trailingPE"),
                    forwardPE=info.get("forwardPE"),
                    dividendYield=info.get("dividendYield"),
                    enterpriseToRevenue=info.get("enterpriseToRevenue"),
                    enterpriseToEbitda=info.get("enterpriseToEbitda"),
                    pegRatio=info.get("pegRatio"),
                    trailingEps=info.get("trailingEps"),
                    forwardEps=info.get("forwardEps"),
                    sector=sector,
                    updated=timezone.now()
                )
            except:
                pass
