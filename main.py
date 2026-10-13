from os.path import join
from bs4 import BeautifulSoup
from collections import Counter
import re
import requests


url = "anti-aging-treatment-toronto"

http_referrer = "https://rejuuvmedispa.com/anti-aging-treatment-toronto/?utm_source=adwords&utm_medium=%7Badname%7D&utm_campaign=%7Bcampaignname%7D&utm_content=%7Badgroupname%7D&campaign_id=23926160377&ad_group_id=200006549249&ad_id=827091137672&gad_source=1&gad_campaignid=23926160377&gbraid=0AAAAAp3a7oG81emhMfP9WzpAqLaWk3eRu&gclid=EAIaIQobChMI5KOOv6KrlwMV9plmAh34zjv1EAAYAiAAEgLBrvD_BwE"

def page_finder(page_name, meta_url):
    arrayed_url = page_name.split("-")

    arrayed_http_referrer = meta_url.replace("/", "-").split("-")
    page = []
    for word in arrayed_url:
        for element in arrayed_http_referrer:
            if element == word:
                page.append(element)

    return " ".join(page)

# print(page_finder(url, http_referrer))
def bulky_split(string, replacement):
    compressor = []
    word_list = []
    counter = 0
    for character in string:
        counter += 1
        if character != replacement:
            compressor.append(character)
        if character == replacement:
            word_list.append("".join(compressor))
            compressor = []
        if len(string) == counter:
            word_list.append("".join(compressor))
            compressor = []

    return word_list

# print(bulky_split(url, "-"))

battle_log = '''
Battle against ShadowSlayer E begins.
[1]: Bane Revolver applied to ShadowSlayer E.
[1]: Fleshweaving applied to Daniell.
[1]: Overflowing Souls applied to Daniell.
[1]: Daniell used skill: Flesh of Ice.
[1]: Daniell recovers 245 MP.
[1]: Flesh Aegis applied to Daniell.
[1]: Daniell critically hits ShadowSlayer E for 133 Ice Magic damage with 64 Bonus and 75 Crit.
[1]: Daniell critically hits ShadowSlayer E for 137 Ice Magic damage with 64 Bonus and 75 Crit.
[1]: Fita used skill: Tickles.
[1]: Tickles! applied to ShadowSlayer E.
[1]: Focused Hunt applied to ShadowSlayer E.
[1]: Slayer Combo applied to ShadowSlayer E.
[1]: ShadowSlayer E misses Daniell with a Pierce attack with 93 Bonus.
[1]: ShadowSlayer E glances Daniell for 0 Silver Pierce damage with 93 Bonus and -19 Crit, reduced by 6.
[1]: Daniell takes 6 damage to MP.
[2]: Daniell used skill: Erupt Horror.
[2]: Daniell recovers 445 MP.
[2]: Body Horror applied to Daniell.
[2]: Daniell critically hits ShadowSlayer E for 288 Ice Magic damage with 164 Bonus and 270 Crit.
[2]: Daniell critically hits ShadowSlayer E for 290 Ice Magic damage with 164 Bonus and 270 Crit.
[2]: Daniell critically hits ShadowSlayer E for 290 Ice Magic damage with 164 Bonus and 270 Crit.
[2]: Daniell critically hits ShadowSlayer E for 288 Ice Magic damage with 164 Bonus and 270 Crit.
[2]: Fita used skill: Overcharge.
[2]: Dragon Overcharge applied to Daniell.
[2]: ShadowSlayer E misses Daniell with a Pierce attack with 93 Bonus.
[2]: ShadowSlayer E glances Daniell for 0 Silver Pierce damage with 93 Bonus and -19 Crit, reduced by 6.
[2]: Daniell takes 6 damage to MP.
[3]: Daniell used skill: Flesh of Fire.
[3]: Daniell recovers 245 MP.
[3]: Overwhelming Hunger applied to Daniell.
[3]: Daniell critically hits ShadowSlayer E for 213 Ice Magic damage with 164 Bonus and 265 Crit.
[3]: Daniell critically hits ShadowSlayer E for 205 Ice Magic damage with 164 Bonus and 265 Crit.
[3]: Daniell critically hits ShadowSlayer E for 218 Ice Magic damage with 164 Bonus and 265 Crit.
[3]: Daniell critically hits ShadowSlayer E for 218 Ice Magic damage with 164 Bonus and 265 Crit.
[3]: Daniell critically hits ShadowSlayer E for 215 Ice Magic damage with 164 Bonus and 265 Crit.
[3]: Daniell critically hits ShadowSlayer E for 213 Ice Magic damage with 164 Bonus and 265 Crit.
[3]: Fita used skill: Heal Ally.
[3]: Daniell recovers 367 HP.
[3]: Tickles! fades from ShadowSlayer E.
[3]: ShadowSlayer E misses Daniell with a Pierce attack with 93 Bonus.
[3]: ShadowSlayer E misses Daniell with a Pierce attack with 93 Bonus.
[3]: ShadowSlayer E misses Daniell with a Pierce attack with 93 Bonus.
[4]: Flesh Aegis fades from Daniell.
[4]: Daniell takes 200 damage.
[4]: Daniell recovers 200 MP.
[4]: Daniell used skill: Flesh of Energy.
[4]: Lightning Vector applied to Daniell.
[4]: Daniell critically hits ShadowSlayer E for 734 Ice Magic damage with 164 Bonus and 465 Crit.
[4]: Daniell critically hits ShadowSlayer E for 711 Ice Magic damage with 164 Bonus and 465 Crit.
[4]: Fita used skill: Noxious Fumes.
[4]: Noxious Fumes applied to ShadowSlayer E.
[4]: Fita hits ShadowSlayer E for 92 Ice Magic damage with 65 Bonus and 10 Crit.
[4]: Dragon Fumes applied to ShadowSlayer E.
[4]: Dragon Fumes fades from ShadowSlayer E.
[4]: Focused Hunt fades from ShadowSlayer E.
[4]: Noxious Fumes fades from ShadowSlayer E.
[4]: ShadowSlayer E hits Daniell for 0 Silver Pierce damage with 63 Bonus and 31 Crit, reduced by 60.
[4]: Daniell takes 60 damage to MP.
[4]: ShadowSlayer E hits Daniell for 0 Silver Pierce damage with 63 Bonus and 31 Crit, reduced by 57.
[4]: Daniell takes 57 damage to MP.
[4]: ShadowSlayer E hits Daniell for 0 Silver Pierce damage with 63 Bonus and 31 Crit, reduced by 56.
[4]: Daniell takes 56 damage to MP.
[4]: ShadowSlayer E hits Daniell for 0 Silver Pierce damage with 63 Bonus and 31 Crit, reduced by 56.
[4]: Daniell takes 56 damage to MP.
[4]: ShadowSlayer E hits Daniell for 0 Silver Pierce damage with 63 Bonus and 31 Crit, reduced by 55.
[4]: Daniell takes 55 damage to MP.
[5]: Dragon Overcharge fades from Daniell.
[5]: Lightning Vector fades from Daniell.
[5]: Daniell takes 250 damage.
[5]: Daniell recovers 250 MP.
[5]: Daniell used skill: Flesh of Energy.
[5]: Lightning Vector applied to Daniell.
[5]: Daniell critically hits ShadowSlayer E for 615 Ice Magic damage with 164 Bonus and 465 Crit.
[5]: Daniell critically hits ShadowSlayer E for 635 Ice Magic damage with 164 Bonus and 465 Crit.
[5]: Fita used skill: Dragon's Scales.
[5]: Dragon's Scales applied to Daniell.
[5]: ShadowSlayer E recovers 732 HP.
[5]: ShadowSlayer E misses Daniell with a Pierce attack with 63 Bonus.
[6]: Lightning Vector fades from Daniell.
[6]: Daniell takes 300 damage.
[6]: Daniell recovers 300 MP.
[6]: Daniell used skill: Flesh of Energy.
[6]: Lightning Vector applied to Daniell.
[6]: Daniell critically hits ShadowSlayer E for 671 Ice Magic damage with 164 Bonus and 465 Crit.
[6]: Daniell critically hits ShadowSlayer E for 650 Ice Magic damage with 164 Bonus and 465 Crit.
[6]: Fita used skill: Attack.
[6]: Fita misses ShadowSlayer E with a Magic attack with 65 Bonus.
[6]: ShadowSlayer E misses Daniell with a Pierce attack with 63 Bonus.
[7]: Dragon's Scales fades from Daniell.
[7]: Lightning Vector fades from Daniell.
[7]: Daniell takes 350 damage.
[7]: Daniell recovers 350 MP.
[7]: Daniell used skill: Flesh of Darkness.
[7]: Daniell critically hits ShadowSlayer E for 734 Ice Magic damage with 164 Bonus and 265 Crit.
[7]: Flesh Reaper applied to ShadowSlayer E.
[7]: Fita used skill: Attack.
[7]: Fita hits ShadowSlayer E for 81 Ice Magic damage with 65 Bonus and 10 Crit.
[7]: ShadowSlayer E takes 100 Ice damage from Flesh Reaper.
[7]: Focused Hunt applied to ShadowSlayer E.
[7]: ShadowSlayer E critically hits Daniell for 0 Wind Pierce damage with 63 Bonus and 31 Crit, reduced by 122.
[7]: Daniell takes 122 damage to MP.
[7]: ShadowSlayer E hits Daniell for 0 Silver Pierce damage with 63 Bonus and 31 Crit, reduced by 98.
[7]: Daniell takes 98 damage to MP.
[8]: Daniell takes 400 damage.
[8]: Daniell recovers 400 MP.
[8]: Daniell used skill: Dual Immolation.
[8]: Daniell critically hits ShadowSlayer E for 312 Ice Magic damage with 164 Bonus and 465 Crit.
[8]: Daniell critically hits ShadowSlayer E for 319 Ice Magic damage with 164 Bonus and 465 Crit.
[8]: Daniell critically hits ShadowSlayer E for 317 Ice Magic damage with 164 Bonus and 465 Crit.
[8]: Daniell critically hits ShadowSlayer E for 302 Ice Magic damage with 164 Bonus and 465 Crit.
[8]: Daniell critically hits ShadowSlayer E for 302 Ice Magic damage with 164 Bonus and 465 Crit.
[8]: Daniell critically hits ShadowSlayer E for 312 Ice Magic damage with 164 Bonus and 465 Crit.
[8]: Overwhelming Hunger fades from Daniell.
[8]: Fita used skill: Attack.
[8]: Fita hits ShadowSlayer E for 80 Ice Magic damage with 65 Bonus and 10 Crit.
[8]: ShadowSlayer E takes 94 Ice damage from Flesh Reaper.
[8]: ShadowSlayer E hits Daniell for 0 Wind Pierce damage with 63 Bonus and 31 Crit, reduced by 73.
[8]: Daniell takes 73 damage to MP.
[8]: ShadowSlayer E hits Daniell for 0 Silver Pierce damage with 63 Bonus and 31 Crit, reduced by 39.
[8]: Daniell takes 39 damage to MP.
[8]: ShadowSlayer E hits Daniell for 0 Silver Pierce damage with 63 Bonus and 31 Crit, reduced by 38.
[8]: Daniell takes 38 damage to MP.
[8]: ShadowSlayer E hits Daniell for 0 Silver Pierce damage with 63 Bonus and 31 Crit, reduced by 38.
[8]: Daniell takes 38 damage to MP.
[8]: ShadowSlayer E hits Daniell for 0 Silver Pierce damage with 63 Bonus and 31 Crit, reduced by 38.
[8]: Daniell takes 38 damage to MP.
[8]: ShadowSlayer E hits Daniell for 0 Silver Pierce damage with 63 Bonus and 31 Crit, reduced by 38.
[8]: Daniell takes 38 damage to MP.
[9]: Body Horror fades from Daniell.
[9]: Daniell used skill: Morbid Cage.
[9]: Daniell recovers 245 MP.
[9]: Daniell misses ShadowSlayer E with a Magic attack with 114 Bonus.
[9]: Daniell hits ShadowSlayer E for 50 Ice Magic damage with 114 Bonus and 70 Crit.
[9]: Caged Soul applied to ShadowSlayer E.
[9]: Morbid Cage applied to ShadowSlayer E.
[9]: Morbid Cage fades from ShadowSlayer E.
[9]: Focused Hunt fades from ShadowSlayer E.
[9]: Daniell critically hits ShadowSlayer E for 106 Ice Magic damage with 114 Bonus and 70 Crit.
[9]: Morbid Cage applied to ShadowSlayer E.
[9]: Morbid Cage fades from ShadowSlayer E.
[9]: Daniell critically hits ShadowSlayer E for 110 Ice Magic damage with 114 Bonus and 70 Crit.
[9]: Morbid Cage applied to ShadowSlayer E.
[9]: Morbid Cage fades from ShadowSlayer E.
[9]: Fita used skill: Dragon Scout.
[9]: Dragon Scout applied to Daniell.
[9]: ShadowSlayer E takes 95 Ice damage from Flesh Reaper.
[9]: ShadowSlayer E hits Daniell for 0 Silver Pierce damage with 33 Bonus and 31 Crit, reduced by 46.
[9]: Daniell takes 46 damage to MP.
[9]: ShadowSlayer E hits Daniell for 0 Silver Pierce damage with 33 Bonus and 31 Crit, reduced by 45.
[9]: Daniell takes 45 damage to MP.
[10]: Daniell used skill: Flesh of Water.
[10]: Daniell critically hits ShadowSlayer E for 84 Ice Magic damage with 164 Bonus and 70 Crit.
[10]: Daniell recovers 121 HP.
[10]: Daniell hits ShadowSlayer E for 38 Ice Magic damage with 164 Bonus and 70 Crit.
[10]: Daniell recovers 121 HP.
[10]: Daniell critically hits ShadowSlayer E for 83 Ice Magic damage with 164 Bonus and 70 Crit.
[10]: Daniell recovers 121 HP.
[10]: Fita used skill: Attack.
[10]: Fita hits ShadowSlayer E for 77 Ice Magic damage with 65 Bonus and 10 Crit.
[10]: ShadowSlayer E takes 92 Ice damage from Flesh Reaper.
[10]: ShadowSlayer E hits Daniell for 0 Silver Pierce damage with 33 Bonus and 31 Crit, reduced by 290.
[10]: Daniell takes 290 damage to MP.
[10]: Silverdust applied to Daniell.
[11]: Daniell used skill: Flesh of Ice.
[11]: Daniell recovers 245 MP.
[11]: Flesh Aegis applied to Daniell.
[11]: Daniell hits ShadowSlayer E for 66 Ice Magic damage with 104 Bonus and 70 Crit.
[11]: Daniell hits ShadowSlayer E for 62 Ice Magic damage with 104 Bonus and 70 Crit.
[11]: Fita used skill: Attack.
[11]: Fita hits ShadowSlayer E for 83 Ice Magic damage with 65 Bonus and 10 Crit.
[11]: Flesh Reaper fades from ShadowSlayer E.
[11]: Caged Soul fades from ShadowSlayer E.
[11]: ShadowSlayer E recovers 732 HP.
[11]: ShadowSlayer E misses Daniell with a Pierce attack with 33 Bonus.
[12]: Daniell used skill: Flesh of Nature.
[12]: Rampant Regrowth applied to Daniell.
[12]: Daniell hits ShadowSlayer E for 53 Ice Magic damage with 104 Bonus and 70 Crit.
[12]: The Feast applied to Daniell.
[12]: The Harvest applied to ShadowSlayer E.
[12]: Daniell misses ShadowSlayer E with a Magic attack with 104 Bonus.
[12]: Daniell misses ShadowSlayer E with a Magic attack with 104 Bonus.
[12]: Daniell misses ShadowSlayer E with a Magic attack with 104 Bonus.
[12]: Fita used skill: Attack.
[12]: Fita misses ShadowSlayer E with a Magic attack with 65 Bonus.
[12]: ShadowSlayer E misses Daniell with a Pierce attack with 33 Bonus.
[13]: Silverdust fades from Daniell.
[13]: Flesh Aegis fades from Daniell.
[13]: Daniell recovers 182 HP from Rampant Regrowth.
[13]: Daniell drinks a Health potion.
[13]: Daniell recovers 1254 HP.
[13]: Arachnaboost applied to Daniell.
[13]: Fita used skill: Attack.
[13]: Fita misses ShadowSlayer E with a Magic attack with 65 Bonus.
[13]: Focused Hunt applied to ShadowSlayer E.
[13]: ShadowSlayer E hits Daniell for 0 Wind Pierce damage with 63 Bonus and 31 Crit, reduced by 110.
[13]: Daniell takes 110 damage to MP.
[13]: ShadowSlayer E hits Daniell for 0 Silver Pierce damage with 63 Bonus and 31 Crit, reduced by 149.
[13]: Daniell takes 149 damage to MP.
[14]: Dragon Scout fades from Daniell.
[14]: Daniell recovers 182 HP from Rampant Regrowth.
[14]: Daniell used skill: Hecatoncheires.
[14]: Daniell recovers 295 MP.
[14]: Daniell hits ShadowSlayer E for 39 Ice Magic damage with 64 Bonus and 75 Crit.
[14]: Seized Soul applied to Daniell.
[14]: Inescapable Reach applied to ShadowSlayer E.
[14]: Daniell critically hits ShadowSlayer E for 99 Ice Magic damage with 64 Bonus and 75 Crit.
[14]: Daniell critically hits ShadowSlayer E for 95 Ice Magic damage with 64 Bonus and 75 Crit.
[14]: Daniell critically hits ShadowSlayer E for 99 Ice Magic damage with 64 Bonus and 75 Crit.
[14]: Daniell critically hits ShadowSlayer E for 96 Ice Magic damage with 64 Bonus and 75 Crit.
[14]: Daniell hits ShadowSlayer E for 48 Ice Magic damage with 64 Bonus and 75 Crit.
[14]: Fita used skill: Attack.
[14]: Fita hits ShadowSlayer E for 93 Ice Magic damage with 65 Bonus and 10 Crit.
[14]: ShadowSlayer E hits Daniell for 0 Wind Pierce damage with 63 Bonus and 31 Crit, reduced by 117.
[14]: Daniell takes 117 damage to MP.
[14]: ShadowSlayer E hits Daniell for 0 Silver Pierce damage with 63 Bonus and 31 Crit, reduced by 154.
[14]: Daniell takes 154 damage to MP.
[15]: Daniell recovers 182 HP from Rampant Regrowth.
[15]: Daniell used skill: Erupt Horror.
[15]: Daniell recovers 445 MP.
[15]: Body Horror applied to Daniell.
[15]: Daniell critically hits ShadowSlayer E for 328 Ice Magic damage with 164 Bonus and 275 Crit.
[15]: Daniell critically hits ShadowSlayer E for 312 Ice Magic damage with 164 Bonus and 275 Crit.
[15]: Daniell critically hits ShadowSlayer E for 312 Ice Magic damage with 164 Bonus and 275 Crit.
[15]: Daniell critically hits ShadowSlayer E for 328 Ice Magic damage with 164 Bonus and 275 Crit.
[15]: ShadowSlayer E's HP was adjusted.
[15]: Fita used skill: Attack.
[15]: Fita hits ShadowSlayer E for 0 Ice Magic damage with 65 Bonus and 10 Crit.
[15]: The Harvest fades from ShadowSlayer E.
[15]: Final Draught applied to ShadowSlayer E.
[15]: ShadowSlayer E's HP was adjusted.
[15]: ShadowSlayer E critically hits Daniell for 0 Wind Pierce damage with 93 Bonus and 46 Crit, reduced by 264.
[15]: Daniell takes 264 damage to MP.
[15]: ShadowSlayer E hits Daniell for 0 Silver Pierce damage with 93 Bonus and 46 Crit, reduced by 94.
[15]: Daniell takes 94 damage to MP.
[15]: Mortalbane applied to Daniell.
[15]: ShadowSlayer E hits Daniell for 0 Silver Pierce damage with 93 Bonus and 46 Crit, reduced by 108.
[15]: Daniell takes 108 damage to MP.
[15]: Mortalbane fades from Daniell.
[15]: Daniell recovers 182 HP from Rampant Regrowth.
[15]: Daniell used skill: Erupt Horror.
[15]: Daniell recovers 445 MP.
[15]: Body Horror applied to Daniell.
[15]: Daniell critically hits ShadowSlayer E for 315 Ice Magic damage with 164 Bonus and 270 Crit.
[15]: Daniell critically hits ShadowSlayer E for 322 Ice Magic damage with 164 Bonus and 270 Crit.
[15]: ShadowSlayer E's HP was adjusted.
[15]: Daniell critically hits ShadowSlayer E for 0 Ice Magic damage with 164 Bonus and 270 Crit.
[15]: Daniell critically hits ShadowSlayer E for 0 Ice Magic damage with 164 Bonus and 270 Crit.
[15]: Fita used skill: Attack.
[15]: Fita misses ShadowSlayer E with a Magic attack with 65 Bonus.
[15]: The Harvest fades from ShadowSlayer E.
[15]: Final Draught applied to ShadowSlayer E.
[15]: ShadowSlayer E's HP was adjusted.
[15]: ShadowSlayer E hits Daniell for 0 Wind Pierce damage with 93 Bonus and 46 Crit, reduced by 141.
[15]: Daniell takes 141 damage to MP.
[15]: ShadowSlayer E hits Daniell for 0 Silver Pierce damage with 93 Bonus and 46 Crit, reduced by 87.
[15]: Daniell takes 87 damage to MP.
[15]: Swarmbane applied to Fita.
[15]: ShadowSlayer E hits Daniell for 0 Silver Pierce damage with 93 Bonus and 46 Crit, reduced by 95.
[15]: Daniell takes 95 damage to MP.
[16]: Rampant Regrowth fades from Daniell.
[16]: The Feast fades from Daniell.
[16]: Daniell used skill: Flesh of Darkness.
[16]: Daniell critically hits ShadowSlayer E for 518 Ice Magic damage with 164 Bonus and 270 Crit.
[16]: Flesh Reaper applied to ShadowSlayer E.
[16]: Fita is immobilized by Swarmbane.
[16]: ShadowSlayer E takes 1465 Poison damage from Final Draught.
[16]: ShadowSlayer E takes 93 Ice damage from Flesh Reaper.
[16]: ShadowSlayer E critically hits Daniell for 79 Wind Pierce damage with 93 Bonus and 61 Crit, reduced by 122.
[16]: Daniell takes 22 damage to MP.
[16]: ShadowSlayer E hits Daniell for 60 Silver Pierce damage with 93 Bonus and 61 Crit.
[16]: ShadowSlayer E critically hits Daniell for 105 Silver Pierce damage with 93 Bonus and 61 Crit.
[16]: ShadowSlayer E critically hits Daniell for 111 Silver Pierce damage with 93 Bonus and 61 Crit.
[16]: ShadowSlayer E critically hits Daniell for 112 Silver Pierce damage with 93 Bonus and 61 Crit.
[16]: ShadowSlayer E hits Daniell for 58 Silver Pierce damage with 93 Bonus and 61 Crit.
[17]: Daniell drinks a Mana potion.
[17]: Daniell recovers 415 MP.
[17]: Swarmbane fades from Fita.
[17]: Fita used skill: Attack.
[17]: Fita glances ShadowSlayer E for 4 Ice Magic damage with 65 Bonus and 10 Crit.
[17]: ShadowSlayer E takes 1465 Poison damage from Final Draught.
[17]: ShadowSlayer E takes 92 Ice damage from Flesh Reaper.
[17]: Inescapable Reach fades from ShadowSlayer E.
[17]: Flesh Reaper fades from ShadowSlayer E.
[17]: ShadowSlayer E hits Daniell for 0 Wind Pierce damage with 93 Bonus and 91 Crit, reduced by 173.
[17]: Daniell takes 173 damage to MP.
[17]: ShadowSlayer E recovers 732 HP.
[17]: ShadowSlayer E hits Daniell for 711 Silver Pierce damage with 93 Bonus and 41 Crit, reduced by 242.
[17]: Daniell takes 242 damage to MP.
[18]: Daniell used skill: Flesh of Ice.
[18]: Daniell recovers 245 MP.
[18]: Flesh Aegis applied to Daniell.
[18]: Daniell critically hits ShadowSlayer E for 128 Ice Magic damage with 164 Bonus and 270 Crit.
[18]: Daniell critically hits ShadowSlayer E for 131 Ice Magic damage with 164 Bonus and 270 Crit.
[18]: Fita used skill: Heal Ally.
[18]: Daniell recovers 367 HP.
[18]: ShadowSlayer E takes 1465 Poison damage from Final Draught.
[18]: ShadowSlayer E misses Daniell with a Pierce attack with 93 Bonus.
[18]: ShadowSlayer E misses Daniell with a Pierce attack with 93 Bonus.
[19]: Arachnaboost fades from Daniell.
[19]: Daniell drinks a Health potion.
[19]: Daniell recovers 1045 HP.
[19]: Arachnaboost applied to Daniell.
[19]: Fita used skill: Dragon Scout.
[19]: Dragon Scout applied to Daniell.
[19]: Focused Hunt fades from ShadowSlayer E.
[19]: ShadowSlayer E takes 1465 Poison damage from Final Draught.
[19]: Focused Hunt applied to ShadowSlayer E.
[19]: ShadowSlayer E critically glances Daniell for 0 Wind Pierce damage with 93 Bonus and 271 Crit, reduced by 140.
[19]: Daniell takes 140 damage to MP.
[19]: ShadowSlayer E misses Daniell with a Pierce attack with 93 Bonus.
[20]: Daniell used skill: Flesh of Fire.
[20]: Daniell recovers 245 MP.
[20]: Overwhelming Hunger applied to Daniell.
[20]: Daniell critically hits ShadowSlayer E for 176 Ice Magic damage with 264 Bonus and 270 Crit.
[20]: Daniell critically hits ShadowSlayer E for 175 Ice Magic damage with 264 Bonus and 270 Crit.
[20]: Daniell critically hits ShadowSlayer E for 179 Ice Magic damage with 264 Bonus and 270 Crit.
[20]: Daniell critically hits ShadowSlayer E for 180 Ice Magic damage with 264 Bonus and 270 Crit.
[20]: Daniell critically hits ShadowSlayer E for 185 Ice Magic damage with 264 Bonus and 270 Crit.
[20]: Daniell critically hits ShadowSlayer E for 176 Ice Magic damage with 264 Bonus and 270 Crit.
[20]: Fita used skill: Attack.
[20]: Fita hits ShadowSlayer E for 70 Ice Magic damage with 65 Bonus and 10 Crit.
[20]: ShadowSlayer E takes 1465 Poison damage from Final Draught.
[20]: ShadowSlayer E misses Daniell with a Pierce attack with 93 Bonus.
[20]: ShadowSlayer E critically hits Daniell for 0 Silver Pierce damage with 93 Bonus and 511 Crit, reduced by 130.
[20]: Daniell takes 130 damage to MP.
[20]: ShadowSlayer E misses Daniell with a Pierce attack with 93 Bonus.
[20]: ShadowSlayer E misses Daniell with a Pierce attack with 93 Bonus.
[20]: ShadowSlayer E misses Daniell with a Pierce attack with 93 Bonus.
[20]: ShadowSlayer E misses Daniell with a Pierce attack with 93 Bonus.
[21]: Flesh Aegis fades from Daniell.
[21]: Daniell takes 400 damage.
[21]: Daniell recovers 400 MP.
[21]: Daniell used skill: Flesh of Energy.
[21]: Lightning Vector applied to Daniell.
[21]: Daniell critically hits ShadowSlayer E for 661 Ice Magic damage with 264 Bonus and 465 Crit.
[21]: Daniell critically hits ShadowSlayer E for 651 Ice Magic damage with 264 Bonus and 465 Crit.
[21]: Fita used skill: Tickles.
[21]: Tickles! applied to ShadowSlayer E.
[21]: ShadowSlayer E takes 1465 Poison damage from Final Draught.
[21]: ShadowSlayer E critically hits Daniell for 0 Wind Pierce damage with 93 Bonus and 941 Crit, reduced by 216.
[21]: Daniell takes 216 damage to MP.
[21]: ShadowSlayer E critically hits Daniell for 0 Silver Pierce damage with 93 Bonus and 941 Crit, reduced by 147.
[21]: Daniell takes 147 damage to MP.
[21]: Revenantbane applied to Daniell.
[21]: ShadowSlayer E critically hits Daniell for 90 Silver Pierce damage with 93 Bonus and 941 Crit, reduced by 57.
[21]: Daniell takes 57 damage to MP.
[22]: Seized Soul fades from Daniell.
[22]: Body Horror fades from Daniell.
[22]: Lightning Vector fades from Daniell.
[22]: Daniell takes 450 damage.
[22]: Daniell recovers 450 MP.
[22]: Daniell used skill: Flesh of Energy.
[22]: Lightning Vector applied to Daniell.
[22]: Daniell critically hits ShadowSlayer E for 651 Ice Magic damage with 164 Bonus and 265 Crit.
[22]: Daniell critically hits ShadowSlayer E for 681 Ice Magic damage with 164 Bonus and 265 Crit.
[22]: Fita used skill: Overcharge.
[22]: Dragon Overcharge applied to Daniell.
[22]: ShadowSlayer E takes 1465 Poison damage from Final Draught.
[22]: ShadowSlayer E critically hits Daniell for 0 Wind Pierce damage with 93 Bonus and 1181 Crit, reduced by 209.
[22]: Daniell takes 209 damage to MP.
[22]: Daniell takes 0 damage to MP.
[22]: ShadowSlayer E critically hits Daniell for 786 Silver Pierce damage with 93 Bonus and 1181 Crit, reduced by 41.
[22]: ShadowSlayer E defeated Daniell.
[22]: Battle lost.
[22]: Daniell's HP was adjusted.

'''

# print(battle_log.split("\n"))
def battle_log_filter(logs):

    skills = []
    for log in logs.split("\n"):
        if "Daniell used skill" in log or "Fita used skill" in log or "Daniell drink" in log:
            skills.append(log)

    return skills

def facebook_id_identifier(compare, main):
    result = []
    if len(main) == len(compare):
        counter = 0
        for character in compare:
            counter += 1
            if character == main[counter - 1]:
                result.append(f'{character}-match')
            else:
                result.append(f'{character}-Not')

        return result
    else:
        return "IDs does not have the same length"

main = "120232285664150419"
compare = "120232711655590419"

# result = facebook_id_identifier(compare, main)
#
# counter = 0
# for character in result:
#     counter += 1
#     print(f'{character}\t Main: {main[counter - 1]}')

# 1. Fetch and parse the page
rejuuv_url = "https://signaturemedispa.com/"  # Change this to your target site
response = requests.get(rejuuv_url)
soup = BeautifulSoup(response.text, "html.parser")

# 2. Extract clean, human-readable text from the webpage body
# This strips away scripts, CSS styling, and hidden code elements
raw_text = soup.get_text().lower()

# 3. Clean the text and tokenize it into individual clean words
# This regular expression keeps only letters and filters out numbers/punctuation
words = re.findall(r"\b[a-z]{3,}\b", raw_text)


# --- THE COMBINATION ENGINE ---

def get_phrase_combinations(word_list, phrase_length):
    """Slices a list of words into overlapping multi-word phrase combinations."""
    phrases = []
    # Loop through the words to pair up neighboring words
    for i in range(len(word_list) - phrase_length + 1):
        # Join words together based on the desired length (e.g., 2 or 3 words)
        phrase = " ".join(word_list[i: i + phrase_length])
        phrases.append(phrase)
    return phrases


# 4. Generate 2-word and 3-word phrase combinations
two_word_phrases = get_phrase_combinations(words, 2)
three_word_phrases = get_phrase_combinations(words, 3)
four_word_phrases = get_phrase_combinations(words, 4)

# 5. Count frequencies using Python's Counter tool
top_2_word_keywords = Counter(two_word_phrases).most_common(10)
top_3_word_keywords = Counter(three_word_phrases).most_common(10)
top_4_word_keywords = Counter(four_word_phrases).most_common(10)

# --- DISPLAY RESULTS ---
print("=== TOP 10 TWO-WORD COMBINATIONS ===")
for phrase, count in top_2_word_keywords:
    print(f"[{count}x] {phrase}")

print("\n=== TOP 10 THREE-WORD COMBINATIONS ===")
for phrase, count in top_3_word_keywords:
    print(f"[{count}x] {phrase}")

print("\n=== TOP 10 FOUR-WORD COMBINATIONS ===")
for phrase, count in top_4_word_keywords:
    print(f"[{count}x] {phrase}")

print(f"words len: {len(words)} {len(words) * 0.02}")


