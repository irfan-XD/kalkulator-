#scrip by irfan azhura XD
#100% open source code
import os
from rich.panel import Panel
from rich.console import Console
os.system("clear")
Console(width=35, style="bold black").print(Panel("""
[white]╦╔═╔═╗╦  ╦╔═╦ ╦╦  ╔═╗╔╦╗╔═╗╦═╗  
╠╩╗╠═╣║  ╠╩╗║ ║║  ╠═╣ ║ ║ ║╠╦╝  
╩ ╩╩ ╩╩═╝╩ ╩╚═╝╩═╝╩ ╩ ╩ ╚═╝╩╚═  """,title="LOGO"))
Console(width=35, style="bold black").print(Panel("""[bold white][[bold green]1[bold white]]. Penjumlahan 
[bold white][[bold green]2[bold white]]. pengurangan 
[bold white][[bold green]3[bold white]]. perkalian 
[bold white][[bold green]4[bold white]]. pembagian """, title="BY IRFAN AZHURA"))
lah = input(" [Pilih] : ")
if lah in ('1','01'):
  tam = input(' [tambah] : ')
  
  tam2 = input(' [tambah] : ')
  sum = int(tam) + int(tam2)
  
  print(' [Hasil] {0} + {1} = {2}'.format(tam, tam2, sum))
if lah in ('2','02'):
  tam = input(' [kurang] : ')
 
  tam2 = input(' [kurang] : ')
  sum = int(tam) - int(tam2)
 
  print(' [Hasil] {0} - {1} = {2}'.format(tam, tam2, sum))
if lah in ('3','03'):
  tam = input(' [kali] : ')
 
  tam2 = input(' [kali] : ')
  sum = int(tam) * int(tam2)
 
  print(' [Hasil] {0} × {1} = {2}'.format(tam, tam2, sum))
if lah in ('4','04'):
  tam = input(' [bagi] : ')
  
  tam2 = input(' [bagi] : ')
  sum = int(tam) / int(tam2)
  
  print(' [Hasil] {0} ÷ {1} = {2}'.format(tam, tam2, sum))
 