import requests, re, bs4

request_obj = requests.get("https://payegan.ir/page/post/")
From_The_Destination = input("لطفا شهر مبدا را وارد نمایید")
To_Destination = input("لطفا شهر مقصد را وارد نمایید")
inputPrice = int(input("لطفا قیمت محصول را وارد نمایید"))
inputWeight = int(input("لطفا وزن محصول را وارد نمایید"))
Destination_From_Request = requests.get(
    "https://payeganltd.com/backend/web/index.php?r=site%2Fcity_list&just_state=3&id=1&q=" + From_The_Destination)
Destination_To_Request = requests.get(
    "https://payeganltd.com/backend/web/index.php?r=site%2Fcity_list&just_state=3&id=1&q=" + To_Destination)
if Destination_From_Request.status_code == 200 and Destination_To_Request.status_code == 200:
    From_The_Destination_Json = Destination_From_Request.json()
    To_The_Destination_Json = Destination_To_Request.json()
    if len(From_The_Destination_Json.get("results")) > 0 and len(To_The_Destination_Json.get("results")) > 0:
        form_data = {
            "from_id": From_The_Destination_Json.get("results")[0].get("id"),
            "to_id": To_The_Destination_Json.get("results")[0].get("id"),
            "inputWeight": inputWeight,
            "inputPrice": inputPrice,
            "PayType": 1,
        }
        Response_Html = requests.post("https://payegan.ir/page/post/", data=form_data).content
        Bs_Object = bs4.BeautifulSoup(Response_Html, "html.parser")
        result_list = list(
            Bs_Object.find("div", attrs={"id": "getresponse"}).find("div", attrs={"class": "form-group"}).children)
        new_result_list = list(item for item in result_list if item != "\n")
        for item in new_result_list:
            print(item.text)
    else:
        print("Not Found")
else:
    print("Connection Error")
