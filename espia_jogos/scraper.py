from typing import List

from bs4 import BeautifulSoup
import requests


class Scraper:
    base_url = "https://www.ludopedia.com.br"

    @classmethod
    def usuarios_do_grupo(cls, group: int) -> List[str]:
        endpoint = f"{cls.base_url}/grupo/{group}"
        response = requests.get(endpoint)
        if response.status_code != 200:
            print(f"Erro ao buscar dados: {response.status_code}")
            return []
        soup = BeautifulSoup(response.content, "html.parser")
        users = soup.find(class_="caixa").find_all("a")
        return [user.text for user in users]
