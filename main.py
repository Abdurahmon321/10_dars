# 1 - masala
# import threading
# import multiprocessing
# import time
#
#
# def sum_numbers(n):
#     total = 0
#     while n > 0:
#         total += n % 10
#         n //= 10
#     print("raqamlar yig'indisi: ", total)
#
#
# def main():
#     numbers = []
#     while True:
#         n = input("Son kiriting: ")
#         if n == "stop":
#             break
#         else:
#             numbers.append(int(n))
#
#     threads = []
#
#     start = time.time()
#
#     for i in numbers:
#         th = threading.Thread(target=sum_numbers, args=(i,))
#         threads.append(th)
#         th.start()
#     for i in threads:
#         i.join()
#
#     end = time.time()
#
#     print(f"threads ishlashi uchun ketgan vaqt {round(end-start, 10)}")
#
#     start = time.time()
#     processes = []
#
#     for i in numbers:
#         pr = multiprocessing.Process(target=sum_numbers, args=(i,))
#         processes.append(pr)
#         pr.start()
#
#     for i in processes:
#         i.join()
#
#     end = time.time()
#
#     print(f"multi proccesing ishlashi uchun ketgan vaqt {round(end-start, 10)}")
#
#
# if __name__ == "__main__":
#     main()
#
# 2- masala --------------------------------------------------------------------------------
# import multiprocessing
# import threading
# import time
#
#
# def seconds_to_time(second):
#     first_second = second
#     day = second // 86400
#     second = second % 86400
#     hour = second // 3600
#     second = second % 3600
#     minut = second // 60
#     second = second % 60
#     print(f"Berilgan sekund {first_second} = {day} kun {hour} soat {minut} sekund {second} ga teng")
#
#
# def main():
#     seconds = []
#     while True:
#         second = input("Sekundli qiymat kiriting: ")
#         if second == "stop":
#             break
#         else:
#             seconds.append(int(second))
#     threads = []
#
#     start = time.time()
#
#     print()
#
#     for i in seconds:
#         th = threading.Thread(target=seconds_to_time, args=(i,))
#         threads.append(th)
#         th.start()
#
#     for th in threads:
#         th.join()
#
#     end = time.time()
#
#     print(f"\nthreads yordamida vaqtlarni ajratish uchun ketgan vaqt {round(end-start, 10)}")
#
#     print()
#
#     processes = []
#
#     start = time.time()
#
#     for i in seconds:
#         pr = multiprocessing.Process(target=seconds_to_time, args=(i,))
#         processes.append(pr)
#         pr.start()
#
#     for pr in processes:
#         pr.join()
#
#     end = time.time()
#
#     print(f"\nmulti processing yordamida vaqtlarni ajratish uchun ketgan vaqt {round(end-start, 10)}")
#
#
# if __name__ == "__main__":
#     main()
#
# 3- masala --------------------------------------------------------------------------------
# import time
# from concurrent import futures
# names = ["alfred", "tabitha", "william", "arla"]
#
#
# def main():
#     start = time.time()
#
#     with futures.ThreadPoolExecutor() as executor:
#         results = executor.map(str.title, names)
#
#     end = time.time()
#
#     print(f"threads ishlashi uchun ketgan vaqt {round(end-start, 10)}\n", list(results))
#
#     start = time.time()
#
#     with futures.ProcessPoolExecutor() as executor:
#         results = executor.map(str.title, names)
#
#     end = time.time()
#
#     print(f"multi proccessinf ishlashi uchun ketgan vaqt {round(end-start, 10)}\n", list(results))
#
#
# if __name__ == "__main__":
#     main()
#
# 4- masala ----------------------------------------------------------------------
# import time
# from concurrent import futures
# scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
#
#
# def scores_75(score):
#     if score > 75:
#         return score
#
#
# def main():
#
#     with futures.ThreadPoolExecutor() as executor:
#         results = filter(lambda score:  score > 75, scores)
#     #     results = executor.map(scores_75, scores)
#     #
#     # filtered_results = [result for result in results if result is not None]
#     #
#     # print(list(filtered_results))
#     print(list(results))
#
#
# if __name__ == "__main__":
#     main()
#
# 5 -masala -----------------------------------------------------------------------
# from concurrent import futures
# words = ['Anna', "Alexey", "Alla", "Kazak", "Dom"]
#
# def main():
#
#     with futures.ThreadPoolExecutor() as executor:
#         results = filter(lambda word: str(word).lower() == str(word[::-1]).lower(), words)
#
#     print(list(results))
#
#
# if __name__ == "__main__":
#     main()
#
# 6 - masala -----------------------------------------------------------
# import multiprocessing
# import threading
# import time
#
# from get_weather_info import weather
#
#
# def main():
#     cities = []
#     while True:
#         city = input("shahar kiriting: ")
#         if city == "stop":
#             break
#         else:
#             cities.append(city)
#
#     threads = []
#
#     start = time.time()
#
#     for i in cities:
#         th = threading.Thread(target=weather, args=(i,))
#         threads.append(th)
#         th.start()
#
#     for th in threads:
#         th.join()
#
#     end = time.time()
#
#     print(f"threads ishlashi uchun ketgan vaqt {round(end-start, 10)}")
#
#     processes = []
#
#     start = time.time()
#
#     for i in cities:
#         pr = multiprocessing.Process(target=weather, args=(i,))
#         processes.append(pr)
#         pr.start()
#
#     for pr in processes:
#         pr.join()
#
#     end = time.time()
#
#     print(f"multi processes ishlashi uchun ketgan vaqt {round(end-start, 10)}")
#
#
# if __name__ == "__main__":
#     main()
#
# 7 - masala ---------------------------------------------------------------
# import multiprocessing
# import threading
#
# import qrcode
#
# links = [
#     "https://www.youtube.com",
#     "https://www.instagram.com",
#     "https://www.tiktok.com",
#     "https://www.pinterest.com",
#     "https://www.tradingview.com"
# ]
#
#
# def create_qrcode(link):
#     none, image_name = str(link).split("//")
#
#     qr = qrcode.QRCode(
#         version=1,
#         error_correction=qrcode.constants.ERROR_CORRECT_L,
#         box_size=10,
#         border=4,
#     )
#     qr.add_data(link)
#     qr.make(fit=True)
#
#     img = qr.make_image(fill_color="black", back_color="white")
#     img.save(f"{image_name}.png")
#
#
# def main():
#     threads = []
#     processes = []
#
#     for i in links:
#         th = threading.Thread(target=create_qrcode, args=(i,))
#         threads.append(th)
#         th.start()
#
#     for th in threads:
#         th.join()
#
#     for i in links:
#         pr = multiprocessing.Process(target=create_qrcode, args=(i,))
#         processes.append(pr)
#         pr.start()
#
#     for i in processes:
#         i.join()
#
#
# if __name__ == "__main__":
#     main()
