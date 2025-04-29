
import requests

url = "https://www.mgm.gov.tr/tahmin/il-ve-ilceler.aspx?il=Ankara&ilce=Ke%C3%A7i%C3%B6ren"  # Örnek bir URL (MGM İstanbul)

try:
    response = requests.get(url)
        response.raise_for_status()  # Eğer bir hata oluşursa (4xx veya 5xx status code), bir HTTPError yükseltir.
            html_icerigi = response.text
                print("Sayfa başarıyla indirildi!")
                    # print(html_icerigi) # İndirilen HTML içeriğini görmek için (çok uzun olabilir)
                    except requests.exceptions.RequestException as e:
                        print(f"Bir hata oluştu: {e}")