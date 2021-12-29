from app.adapter import DollarAdapter, RofexAdapter, CmeAdapter, BloombergAdapter
from app.constants import CME_URLS, BLOOMBERG_URLS, FORMAT, TIMEZONE
from datetime import datetime
from pytz import timezone


class DollarService:
    @staticmethod
    def get_nacion_bank_scraping_data() -> dict:
        nacion_bank_data = DollarAdapter.get_nacion_bank_data()
        dollar_value = (
            nacion_bank_data.find("div", id="divisas")
            .find("tbody")
            .find_all("td")[2]
            .text
        )
        dollar_value = round(float(dollar_value), 2)

        return dict(nacion_bank=dollar_value)


class RofexService:
    @staticmethod
    def get_rofex_scraping_data() -> dict:
        rofex_value_list = []
        rofex_data = RofexAdapter.get_rofex_bank_data()
        rofex_values = (
            rofex_data.find("div", {"class": "table-responsive"})
            .find("tbody")
            .find_all("tr")
        )

        for rof in rofex_values:
            rofex = round(float(rof.find_all("td")[1].text), 2)
            rofex_value_list.append(rofex)

        rofex_value_list = rofex_value_list[0:5]

        return dict(
            rofex_M0_Ar_USD=rofex_value_list[0],
            rofex_M1_Ar_USD=rofex_value_list[1],
            rofex_M2_Ar_USD=rofex_value_list[2],
            rofex_M3_Ar_USD=rofex_value_list[3],
            rofex_M4_Ar_USD=rofex_value_list[4],
        )


class CmeService:
    @staticmethod
    def get_cme_scraping_data() -> dict:
        cme_scrap = dict()
        for name_page, url in CME_URLS.items():
            response = CmeAdapter.get_cme_data(url=url)
            cme_value_list = []

            for i in range(6):
                if (i == 0) and (response["quotes"][i]["last"] != "-"):
                    cme_value = response["quotes"][i]["last"]
                else:
                    cme_value = response["quotes"][i]["priorSettle"]

                cme_value = round(float(cme_value), 2)
                cme_value_list.append(cme_value)

            cme_dict = {
                f"{name_page}_M0" : cme_value_list[0],
                f"{name_page}_M1" : cme_value_list[1],
                f"{name_page}_M2" : cme_value_list[2],
                f"{name_page}_M3" : cme_value_list[3],
                f"{name_page}_M4" : cme_value_list[4],
                f"{name_page}_M5" : cme_value_list[5],
            }
            cme_scrap.update({name_page: cme_dict})

        return cme_scrap


class BloombergService:
    @staticmethod
    def get_bloomberg_scraping_data():
        bloomberg_scrap = dict()

        for name_page, url in BLOOMBERG_URLS.items():

            response = BloombergAdapter.get_bloomberg_data(url=url)
            bloomberg_value_list = []

            for i in range(2):
                bloomberg_price = response["fieldDataCollection"][i]["price"]
                bloomberg_priceChange = response["fieldDataCollection"][i]["priceChange1Day"]

                bloomberg_value_list.append(bloomberg_price)
                bloomberg_value_list.append(bloomberg_priceChange)

            bloomberg_scrap[name_page] = bloomberg_value_list

        return bloomberg_scrap


class Datetime:
    @staticmethod
    def get_time() -> dict:
        now_utc = datetime.now(timezone("UTC"))
        now_bs_arg = now_utc.astimezone(timezone(TIMEZONE))
        _datetime = now_bs_arg.strftime(FORMAT)
        return {"datetime": _datetime}
