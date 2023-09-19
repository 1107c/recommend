from crawl import crawl_and_save_images


if __name__ == "__main__":
    menus = {
        "상의": 0,
        "아우터": 1,
        "바지": 2,
        "원피스": 3,
        "스커트": 4,
        "스니커즈": 5,
        "신발": 6,
        "가방": 7,
        "스포츠/용품": 8,
        "모자": 9,
        "양말/레그웨어": 10,
        "속옷": 11,
        "선글라스/안경테": 12,
        "액세서리": 13,
        "시계": 14,
        "주얼리": 15,
    }
    menu_dict = {}
    for index, menu in enumerate(menus):
        menu_dict[menu] = index

    menu = {v: k for k, v in menu_dict.items()}

    colors = [
        "2",
        "1",
        "7",
        "4",
        "6",
        "32",
        "11",
        "39",
        "37",
        "10",
        "9",
        "12",
        "16",
        "56",
        "45",
    ]
    [2, 1, 7, 4, 6, 32, 11, 39, 37, 10, 9, 12, 16, 56, 45]
    # 2:블랙,1:화이트,7:블루,4:브라운,6:그린,32:민트,11:레드,39:라벤더,37:스카이블루,10:핑크,9:옐로우,12:오렌지,16:데님,56:로즈골드45:라이트 핑크
    sub_menus = [
        "니트/스웨터",
        "후드 티셔츠",
        "맨투맨/스웨트셔츠",
        "긴소매 티셔츠",
        "셔츠/블라우스",
        "피케/카라 티셔츠",
        "반소매 티셔츠",
        "민소매 티셔츠",
        "스포츠 상의",
        "후드 집업",
        "블루종/MA-1",
        "레더/라이더스 재킷",
        "트러커 재킷",
        "슈트/블레이저 재킷",
        "카디건",
        "아노락 재킷",
        "플리스/뽀글이",
        "트레이닝 재킷",
        "환절기 코트",
        "겨울 싱글 코트",
        "롱패딩/롱헤비 아우터",
        "숏패딩/숏헤비 아우터",
        "베스트",
        "사파리/헌팅 재킷",
        "나일론/코치 재킷",
        "무스탕/퍼",
        "데님 팬츠",
        "코튼 팬츠",
        "숏 팬츠",
        "레깅스",
        "스포츠 하의",
        "미니 원피스",
        "미디 원피스",
        "맥시 원피스",
        "미니스커트",
        "미디스커트",
        "롱스커트",
        "캔버스/단화",
        "패션스니커즈화",
        "스포츠스니커즈",
        "구두",
        "로퍼",
        "힐/펌프스",
        "플랫 슈즈",
        "샌들",
        "슬리퍼",
        "부츠",
        "백팩",
        "메신저/크로스 백",
        "숄더백",
        "토트백",
        "에코백",
        "파우치 백",
        "지갑/머니클립",
        "수영복/비치웨어",
        "스포츠신발",
        "스포츠가방",
        "스포츠모자",
        "캡/야구모자",
        "헌팅캡/베레모",
        "버킷/사파리햇",
        "비니",
        "양말",
        "스타킹",
        "여성 속옷 상의",
        "여성 속옷 하의",
        "여성 속옷 세트",
        "남성 속옷",
        "홈웨어",
        "안경",
        "선글라스",
        "벨트",
        "넥타이",
        "머플러",
        "스카프/반다나",
        "장갑",
        "디지털",
        "쿼츠 아날로그",
        "팔찌",
        "귀걸이",
        "반지",
        "목걸이/펜던트",
        "헤어 액세서리",
    ]
    sub_dict = {}
    for index, sub in enumerate(sub_menus):
        sub_dict[sub] = index

    sub = {v: k for k, v in sub_dict.items()}
    total_images = 10

    # for sub_menu in [
    #     sub[0],
    #     sub[1],
    #     sub[2],
    #     sub[3],
    #     sub[4],
    #     sub[5],
    #     sub[6],
    #     sub[7],
    #     sub[8],
    # ]:
    #     for color in colors:
    #         output_folder = f"downloaded_images/{menu[0]}/{sub_menu}/"
    #         try:
    #             crawl_and_save_images(
    #                 menu[0], color, sub_menu, total_images, output_folder
    #             )
    #         except Exception as e:
    #             print(f"Error: {str(e)}")
    #             continue

    # for sub_menu in [
    #     # sub[9],
    #     # sub[10],
    #     # sub[11],
    #     # sub[12],
    #     # sub[13],
    #     # sub[14],
    #     # sub[15],
    #     # sub[16],
    #     # sub[17],
    #     # sub[18],
    #     sub[19],
    #     sub[20],
    #     sub[21],
    #     sub[22],
    #     sub[23],
    #     sub[24],
    #     sub[25],
    # ]:
    #     for color in colors:
    #         output_folder = f"downloaded_images/{menu[1]}/{sub_menu}/"
    #         try:
    #             crawl_and_save_images(
    #                 menu[1], color, sub_menu, total_images, output_folder
    #             )
    #         except Exception as e:
    #             print(f"Error: {str(e)}")
    #             continue

    # for sub_menu in [
    #     sub[26],
    #     sub[27],
    #     sub[28],
    #     sub[29],
    #     sub[30],
    # ]:
    #     for color in colors:
    #         output_folder = f"downloaded_images/{menu[2]}/{sub_menu}/"
    #         try:
    #             crawl_and_save_images(
    #                 menu[2], color, sub_menu, total_images, output_folder
    #             )
    #         except Exception as e:
    #             print(f"Error: {str(e)}")
    #             continue

    # for sub_menu in [
    #     sub[31],
    #     sub[32],
    #     sub[33],
    # ]:
    #     for color in colors:
    #         output_folder = f"downloaded_images/{menu[3]}/{sub_menu}/"
    #         try:
    #             crawl_and_save_images(
    #                 menu[3], color, sub_menu, total_images, output_folder
    #             )
    #         except Exception as e:
    #             print(f"Error: {str(e)}")
    #             continue
    # for sub_menu in [
    #     sub[34],
    #     sub[35],
    #     sub[36],
    # ]:
    #     for color in colors:
    #         output_folder = f"downloaded_images/{menu[4]}/{sub_menu}/"
    #         try:
    #             crawl_and_save_images(
    #                 menu[4], color, sub_menu, total_images, output_folder
    #             )
    #         except Exception as e:
    #             print(f"Error: {str(e)}")
    #             continue

    # for sub_menu in [
    #     sub[37],
    #     sub[38],
    #     sub[39],
    # ]:
    #     for color in colors:
    #         output_folder = f"downloaded_images/{menu[5]}/{sub_menu}/"
    #         try:
    #             crawl_and_save_images(menu[5], color, sub_menu, total_images, output_folder)
    #         except Exception as e:
    #             print(f"Error: {str(e)}")
    #             continue

    # for sub_menu in [
    #     sub[40],
    #     sub[41],
    #     sub[42],
    #     sub[43],
    #     sub[44],
    #     sub[45],
    #     sub[46],
    # ]:
    #     for color in colors:
    #         output_folder = f"downloaded_images/{menu[6]}/{sub_menu}/"
    #         try:
    #             crawl_and_save_images(
    #                 menu[6], color, sub_menu, total_images, output_folder
    #             )
    #         except Exception as e:
    #             print(f"Error: {str(e)}")
    #             continue
    # for sub_menu in [
    #     sub[47],
    #     sub[48],
    #     sub[49],
    #     sub[50],
    #     sub[51],
    #     sub[52],
    #     sub[53],
    # ]:
    #     for color in colors:
    #         output_folder = f"downloaded_images/{menu[7]}/{sub_menu}/"
    #         try:
    #             crawl_and_save_images(
    #                 menu[7], color, sub_menu, total_images, output_folder
    #             )
    #         except Exception as e:
    #             print(f"Error: {str(e)}")
    #             continue
    # for sub_menu in [
    #     sub[54],
    #     sub[55],
    #     sub[56],
    #     sub[57],
    # ]:
    #     for color in colors:
    #         output_folder = f"downloaded_images/{menu[8]}/{sub_menu}/"
    #         try:
    #             crawl_and_save_images(
    #                 menu[8], color, sub_menu, total_images, output_folder
    #             )
    #         except Exception as e:
    #             print(f"Error: {str(e)}")
    #             continue
    # for sub_menu in [
    #     sub[58],
    #     sub[59],
    #     sub[60],
    #     sub[61],
    # ]:
    #     for color in colors:
    #         output_folder = f"downloaded_images/{menu[9]}/{sub_menu}/"
    #         try:
    #             crawl_and_save_images(
    #                 menu[9], color, sub_menu, total_images, output_folder
    #             )
    #         except Exception as e:
    #             print(f"Error: {str(e)}")
    #             continue

    # for sub_menu in [
    #     sub[62],
    #     sub[63],
    # ]:
    #     for color in colors:
    #         output_folder = f"downloaded_images/{menu[10]}/{sub_menu}/"
    #         try:
    #             crawl_and_save_images(
    #                 menu[10], color, sub_menu, total_images, output_folder
    #             )
    #         except Exception as e:
    #             print(f"Error: {str(e)}")
    #             continue

    # for sub_menu in [
    #     sub[64],
    #     sub[65],
    #     sub[66],
    #     sub[67],
    #     sub[68],
    # ]:
    #     for color in colors:
    #         output_folder = f"downloaded_images/{menu[11]}/{sub_menu}/"
    #         try:
    #             crawl_and_save_images(
    #                 menu[11], color, sub_menu, total_images, output_folder
    #             )
    #         except Exception as e:
    #             print(f"Error: {str(e)}")
    #             continue

    # for sub_menu in [
    #     sub[69],
    #     # sub[70],
    # ]:
    #     for color in colors:
    #         output_folder = f"downloaded_images/{menu[12]}/{sub_menu}/"
    #         try:
    #             crawl_and_save_images(
    #                 menu[12], color, sub_menu, total_images, output_folder
    #             )
    #         except Exception as e:
    #             print(f"Error: {str(e)}")
    #             continue

    # for sub_menu in [
    #     sub[71],
    #     sub[72],
    #     sub[73],
    #     sub[74],
    #     sub[75],
    # ]:
    #     for color in colors:
    #         output_folder = f"downloaded_images/{menu[13]}/{sub_menu}/"
    #         try:
    #             crawl_and_save_images(
    #                 menu[13], color, sub_menu, total_images, output_folder
    #             )
    #         except Exception as e:
    #             print(f"Error: {str(e)}")
    #             continue
    #
    for sub_menu in [
        # sub[76],
        sub[77],
    ]:
        for color in colors:
            output_folder = f"downloaded_images/{menu[14]}/{sub_menu}/"
            try:
                crawl_and_save_images(
                    menu[14], color, sub_menu, total_images, output_folder
                )
            except Exception as e:
                print(f"Error: {str(e)}")
                continue
    #
    # for sub_menu in [
    #     sub[78],
    #     sub[79],
    #     sub[80],
    #     sub[81],
    #     sub[82],
    # ]:
    #     for color in colors:
    #         output_folder = f"downloaded_images/{menu[15]}/{sub_menu}/"
    #         try:
    #             crawl_and_save_images(
    #                 menu[15], color, sub_menu, total_images, output_folder
    #             )
    #         except Exception as e:
    #             print(f"Error: {str(e)}")
    #             continue
