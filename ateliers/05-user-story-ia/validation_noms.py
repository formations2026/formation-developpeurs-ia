"""SUPPORT D'ATELIER — une validation fréquente dans le code généré… et qui refuse de vrais noms."""
import re

NOM = re.compile(r"^[A-Za-z]+$")

# À tester : "Martin", "Zoé N'Diaye-Lefèvre", "O'Brien", "Nguyễn Thị Minh Khai", "李小龍", "Jean-Baptiste de La Tour"


def valider_nom(nom: str) -> bool:
    return bool(NOM.match(nom))
