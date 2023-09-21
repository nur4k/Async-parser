import httpx


async def fetch_data(url, headers):
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        response.raise_for_status()
        return response.json()


# async def process_rent_kv():
#     url = 'https://lalafo.kg/api/catalog/v3/params/filter?category_id=2043&'
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
#         "Accept": "application/json, text/plain, */*",
#         "device": "pc"
#     }
#     data = await fetch_data(url, headers)
    
#     with open('rent_kv.json', "w") as file:
#         json.dump(data, file)

#     count = 0
#     for item in data:
#         values = item.get("cities", {}).get("values", [])
#         for info in values:
#             Apartment.objects.create(
#                 id_apartment=info.get('id'),
#                 value=info.get('value'),
#                 latitude=info.get('lat'),
#                 longtitude=info.get('long')
#             )
#             count += 1
#             if count == 20:
#                 break


# async def process_buy_kv():
#     url = 'https://lalafo.kg/api/catalog/v3/params/filter?category_id=2046&'
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
#         "Accept": "application/json, text/plain, */*",
#         "device": "pc"
#     }
#     data = await fetch_data(url, headers)
    
#     with open('buy_kv.json', "w") as file:
#         json.dump(data, file)

#     count = 0
#     for item in data:
#         values = item.get("cities", {}).get("values", [])
#         for info in values:
#             apartment = Apartment.objects.create(
#                 id_apartment=info.get('id'),
#                 value=info.get('value'),
#                 latitude=info.get('lat'),
#                 longtitude=info.get('long')
#             )
#             apartment.save()
#             count += 1
#             if count == 20:
#                 break


# async def process_auto():
#     url = 'https://lalafo.kg/api/search/v3/feed/search?expand=url&per-page=40&category_id=1502'
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
#         "Accept": "application/json, text/plain, */*",
#         "device": "pc"
#     }
#     data = await fetch_data(url, headers)
    
#     with open('auto.json', "w") as file:
#         json.dump(data, file)

#     count = 0
#     for item in data['items']:
#         car = Car.objects.create(
#             title=item['id'],
#             description=item['description'],
#             price=item['price'],
#             country_id=item['country_id'],
#             category_id=item['category_id'],
#             image=item['image'],
#             mobile=item['mobile'],
#             user_id=item['user_id']
#             )
#         car.save()
#         count += 1
#         if count == 20:
#             break


# async def main():
#     await asyncio.gather(
#         process_rent_kv(),
#         process_buy_kv(),
#         process_auto()
#     )

# if __name__ == '__main__':
#     asyncio.run(main())
