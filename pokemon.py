from datetime import datetime
from flask import abort
import cv2
import json
import numpy as np
import base64
import requests

host = ""

POKEMONS = {
    "1": {
        "name": "Bulbasaur",
        "src": host + "bulbasaur.png",
    },
    "2": {
        "name": "Ivysaur",
        "src": "ivysaur.png",
    },
    "3": {
        "name": "Venusaur",
        "src": "venusaur.png",
    },
    "4": {
        "name": "Charmander",
        "src": "charmander.png",
    },
    "5": {
        "name": "Charmeleon",
        "src": "charmeleon.png",
    },
    "6": {
        "name": "Charizard",
        "src": "charizard.png",
    },
    "7": {
        "name": "Squirtle",
        "src": "squirtle.png",
    },
    "8": {
        "name": "Wartortle",
        "src": "wartortle.png",
    },
    "9": {
        "name": "Blastoise",
        "src": "blastoise.png",
    },
    "10": {
        "name": "Caterpie",
        "src": "caterpie.png",
    },
    "11": {
        "name": "Metapod",
        "src": "metapod.png",
    },
    "12": {
        "name": "Butterfree",
        "src": "butterfree.png",
    },
    "13": {
        "name": "Weedle",
        "src": "weedle.png",
    },
    "14": {
        "name": "Kakuna",
        "src": "kakuna.png",
    },
    "15": {
        "name": "Beedrill",
        "src": "beedrill.png",
    },
    "16": {
        "name": "Pidgey",
        "src": "pidgey.png",
    },
    "17": {
        "name": "Pidgeotto",
        "src": "pidgeotto.png",
    },
    "18": {
        "name": "Pidgeot",
        "src": "pidgeot.png",
    },
    "19": {
        "name": "Rattata",
        "src": "rattata.png",
    },
    "20": {
        "name": "Raticate",
        "src": "raticate.png",
    },
    "21": {
        "name": "Spearow",
        "src": "spearow.png",
    },
    "22": {
        "name": "Fearow",
        "src": "fearow.png",
    },
    "23": {
        "name": "Ekans",
        "src": "ekans.png",
    },
    "24": {
        "name": "Arbok",
        "src": "arbok.png",
    },
    "25": {
        "name": "Pikachu",
        "src": "pikachu.png",
    },
    "26": {
        "name": "Raichu",
        "src": "raichu.png",
    },
    "27": {
        "name": "Sandshrew",
        "src": "sandshrew.png",
    },
    "28": {
        "name": "Sandslash",
        "src": "sandslash.png",
    },
    "29": {
        "name": "Nidoran♀",
        "src": "nidoran-f.png",
    },
    "30": {
        "name": "Nidorina",
        "src": "nidorina.png",
    },
    "31": {
        "name": "Nidoqueen",
        "src": "nidoqueen.png",
    },
    "32": {
        "name": "Nidoran♂",
        "src": "nidoran-m.png",
    },
    "33": {
        "name": "Nidorino",
        "src": "nidorino.png",
    },
    "34": {
        "name": "Nidoking",
        "src": "nidoking.png",
    },
    "35": {
        "name": "Clefairy",
        "src": "clefairy.png",
    },
    "36": {
        "name": "Clefable",
        "src": "clefable.png",
    },
    "37": {
        "name": "Vulpix",
        "src": "vulpix.png",
    },
    "38": {
        "name": "Ninetales",
        "src": "ninetales.png",
    },
    "39": {
        "name": "Jigglypuff",
        "src": "jigglypuff.png",
    },
    "40": {
        "name": "Wigglytuff",
        "src": "wigglytuff.png",
    },
    "41": {
        "name": "Zubat",
        "src": "zubat.png",
    },
    "42": {
        "name": "Golbat",
        "src": "golbat.png",
    },
    "43": {
        "name": "Oddish",
        "src": "oddish.png",
    },
    "44": {
        "name": "Gloom",
        "src": "gloom.png",
    },
    "45": {
        "name": "Vileplume",
        "src": "vileplume.png",
    },
    "46": {
        "name": "Paras",
        "src": "paras.png",
    },
    "47": {
        "name": "Parasect",
        "src": "parasect.png",
    },
    "48": {
        "name": "Venonat",
        "src": "venonat.png",
    },
    "49": {
        "name": "Venomoth",
        "src": "venomoth.png",
    },
    "50": {
        "name": "Diglett",
        "src": "diglett.png",
    },
    "51": {
        "name": "Dugtrio",
        "src": "dugtrio.png",
    },
    "52": {
        "name": "Meowth",
        "src": "meowth.png",
    },
    "53": {
        "name": "Persian",
        "src": "persian.png",
    },
    "54": {
        "name": "Psyduck",
        "src": "psyduck.png",
    },
    "55": {
        "name": "Golduck",
        "src": "golduck.png",
    },
    "56": {
        "name": "Mankey",
        "src": "mankey.png",
    },
    "57": {
        "name": "Primeape",
        "src": "primeape.png",
    },
    "58": {
        "name": "Growlithe",
        "src": "growlithe.png",
    },
    "59": {
        "name": "Arcanine",
        "src": "arcanine.png",
    },
    "60": {
        "name": "Poliwag",
        "src": "poliwag.png",
    },
    "61": {
        "name": "Poliwhirl",
        "src": "poliwhirl.png",
    },
    "62": {
        "name": "Poliwrath",
        "src": "poliwrath.png",
    },
    "63": {
        "name": "Abra",
        "src": "abra.png",
    },
    "64": {
        "name": "Kadabra",
        "src": "kadabra.png",
    },
    "65": {
        "name": "Alakazam",
        "src": "alakazam.png",
    },
    "66": {
        "name": "Machop",
        "src": "machop.png",
    },
    "67": {
        "name": "Machoke",
        "src": "machoke.png",
    },
    "68": {
        "name": "Machamp",
        "src": "machamp.png",
    },
    "69": {
        "name": "Bellsprout",
        "src": "bellsprout.png",
    },
    "70": {
        "name": "Weepinbell",
        "src": "weepinbell.png",
    },
    "71": {
        "name": "Victreebel",
        "src": "victreebel.png",
    },
    "72": {
        "name": "Tentacool",
        "src": "tentacool.png",
    },
    "73": {
        "name": "Tentacruel",
        "src": "tentacruel.png",
    },
    "74": {
        "name": "Geodude",
        "src": "geodude.png",
    },
    "75": {
        "name": "Graveler",
        "src": "graveler.png",
    },
    "76": {
        "name": "Golem",
        "src": "golem.png",
    },
    "77": {
        "name": "Ponyta",
        "src": "ponyta.png",
    },
    "78": {
        "name": "Rapidash",
        "src": "rapidash.png",
    },
    "79": {
        "name": "Slowpoke",
        "src": "slowpoke.png",
    },
    "80": {
        "name": "Slowbro",
        "src": "slowbro.png",
    },
    "81": {
        "name": "Magnemite",
        "src": "magnemite.png",
    },
    "82": {
        "name": "Magneton",
        "src": "magneton.png",
    },
    "83": {
        "name": "Farfetch'd",
        "src": "farfetchd.png",
    },
    "84": {
        "name": "Doduo",
        "src": "doduo.png",
    },
    "85": {
        "name": "Dodrio",
        "src": "dodrio.png",
    },
    "86": {
        "name": "Seel",
        "src": "seel.png",
    },
    "87": {
        "name": "Dewgong",
        "src": "dewgong.png",
    },
    "88": {
        "name": "Grimer",
        "src": "grimer.png",
    },
    "89": {
        "name": "Muk",
        "src": "muk.png",
    },
    "90": {
        "name": "Shellder",
        "src": "shellder.png",
    },
    "91": {
        "name": "Cloyster",
        "src": "cloyster.png",
    },
    "92": {
        "name": "Gastly",
        "src": "gastly.png",
    },
    "93": {
        "name": "Haunter",
        "src": "haunter.png",
    },
    "94": {
        "name": "Gengar",
        "src": "gengar.png",
    },
    "95": {
        "name": "Onix",
        "src": "onix.png",
    },
    "96": {
        "name": "Drowzee",
        "src": "drowzee.png",
    },
    "97": {
        "name": "Hypno",
        "src": "hypno.png",
    },
    "98": {
        "name": "Krabby",
        "src": "krabby.png",
    },
    "99": {
        "name": "Kingler",
        "src": "kingler.png",
    },
    "100": {
        "name": "Voltorb",
        "src": "voltorb.png",
    },
    "101": {
        "name": "Electrode",
        "src": "electrode.png",
    },
    "102": {
        "name": "Exeggcute",
        "src": "exeggcute.png",
    },
    "103": {
        "name": "Exeggutor",
        "src": "exeggutor.png",
    },
    "104": {
        "name": "Cubone",
        "src": "cubone.png",
    },
    "105": {
        "name": "Marowak",
        "src": "marowak.png",
    },
    "106": {
        "name": "Hitmonlee",
        "src": "hitmonlee.png",
    },
    "107": {
        "name": "Hitmonchan",
        "src": "hitmonchan.png",
    },
    "108": {
        "name": "Lickitung",
        "src": "lickitung.png",
    },
    "109": {
        "name": "Koffing",
        "src": "koffing.png",
    },
    "110": {
        "name": "Weezing",
        "src": "weezing.png",
    },
    "111": {
        "name": "Rhyhorn",
        "src": "rhyhorn.png",
    },
    "112": {
        "name": "Rhydon",
        "src": "rhydon.png",
    },
    "113": {
        "name": "Chansey",
        "src": "chansey.png",
    },
    "114": {
        "name": "Tangela",
        "src": "tangela.png",
    },
    "115": {
        "name": "Kangaskhan",
        "src": "kangaskhan.png",
    },
    "116": {
        "name": "Horsea",
        "src": "horsea.png",
    },
    "117": {
        "name": "Seadra",
        "src": "seadra.png",
    },
    "118": {
        "name": "Goldeen",
        "src": "goldeen.png",
    },
    "119": {
        "name": "Seaking",
        "src": "seaking.png",
    },
    "120": {
        "name": "Staryu",
        "src": "staryu.png",
    },
    "121": {
        "name": "Starmie",
        "src": "starmie.png",
    },
    "122": {
        "name": "Mr. Mime",
        "src": "mr-mime.png",
    },
    "123": {
        "name": "Scyther",
        "src": "scyther.png",
    },
    "124": {
        "name": "Jynx",
        "src": "jynx.png",
    },
    "125": {
        "name": "Electabuzz",
        "src": "electabuzz.png",
    },
    "126": {
        "name": "Magmar",
        "src": "magmar.png",
    },
    "127": {
        "name": "Pinsir",
        "src": "pinsir.png",
    },
    "128": {
        "name": "Tauros",
        "src": "tauros.png",
    },
    "129": {
        "name": "Magikarp",
        "src": "magikarp.png",
    },
    "130": {
        "name": "Gyarados",
        "src": "gyarados.png",
    },
    "131": {
        "name": "Lapras",
        "src": "lapras.png",
    },
    "132": {
        "name": "Ditto",
        "src": "ditto.png",
    },
    "133": {
        "name": "Eevee",
        "src": "eevee.png",
    },
    "134": {
        "name": "Vaporeon",
        "src": "vaporeon.png",
    },
    "135": {
        "name": "Jolteon",
        "src": "jolteon.png",
    },
    "136": {
        "name": "Flareon",
        "src": "flareon.png",
    },
    "137": {
        "name": "Porygon",
        "src": "porygon.png",
    },
    "138": {
        "name": "Omanyte",
        "src": "omanyte.png",
    },
    "139": {
        "name": "Omastar",
        "src": "omastar.png",
    },
    "140": {
        "name": "Kabuto",
        "src": "kabuto.png",
    },
    "141": {
        "name": "Kabutops",
        "src": "kabutops.png",
    },
    "142": {
        "name": "Aerodactyl",
        "src": "aerodactyl.png",
    },
    "143": {
        "name": "Snorlax",
        "src": "snorlax.png",
    },
    "144": {
        "name": "Articuno",
        "src": "articuno.png",
    },
    "145": {
        "name": "Zapdos",
        "src": "zapdos.png",
    },
    "146": {
        "name": "Moltres",
        "src": "moltres.png",
    },
    "147": {
        "name": "Dratini",
        "src": "dratini.png",
    },
    "148": {
        "name": "Dragonair",
        "src": "dragonair.png",
    },
    "149": {
        "name": "Dragonite",
        "src": "dragonite.png",
    },
    "150": {
        "name": "Mewtwo",
        "src": "mewtwo.png",
    },
    "151": {
        "name": "Mew",
        "src": "mew.png",
    },
    "152": {
        "name": "Chikorita",
        "src": "chikorita.png",
    },
    "153": {
        "name": "Bayleef",
        "src": "bayleef.png",
    },
    "154": {
        "name": "Meganium",
        "src": "meganium.png",
    },
    "155": {
        "name": "Cyndaquil",
        "src": "cyndaquil.png",
    },
    "156": {
        "name": "Quilava",
        "src": "quilava.png",
    },
    "157": {
        "name": "Typhlosion",
        "src": "typhlosion.png",
    },
    "158": {
        "name": "Totodile",
        "src": "totodile.png",
    },
    "159": {
        "name": "Croconaw",
        "src": "croconaw.png",
    },
    "160": {
        "name": "Feraligatr",
        "src": "feraligatr.png",
    },
    "161": {
        "name": "Sentret",
        "src": "sentret.png",
    },
    "162": {
        "name": "Furret",
        "src": "furret.png",
    },
    "163": {
        "name": "Hoothoot",
        "src": "hoothoot.png",
    },
    "164": {
        "name": "Noctowl",
        "src": "noctowl.png",
    },
    "165": {
        "name": "Ledyba",
        "src": "ledyba.png",
    },
    "166": {
        "name": "Ledian",
        "src": "ledian.png",
    },
    "167": {
        "name": "Spinarak",
        "src": "spinarak.png",
    },
    "168": {
        "name": "Ariados",
        "src": "ariados.png",
    },
    "169": {
        "name": "Crobat",
        "src": "crobat.png",
    },
    "170": {
        "name": "Chinchou",
        "src": "chinchou.png",
    },
    "171": {
        "name": "Lanturn",
        "src": "lanturn.png",
    },
    "172": {
        "name": "Pichu",
        "src": "pichu.png",
    },
    "173": {
        "name": "Cleffa",
        "src": "cleffa.png",
    },
    "174": {
        "name": "Igglybuff",
        "src": "igglybuff.png",
    },
    "175": {
        "name": "Togepi",
        "src": "togepi.png",
    },
    "176": {
        "name": "Togetic",
        "src": "togetic.png",
    },
    "177": {
        "name": "Natu",
        "src": "natu.png",
    },
    "178": {
        "name": "Xatu",
        "src": "xatu.png",
    },
    "179": {
        "name": "Mareep",
        "src": "mareep.png",
    },
    "180": {
        "name": "Flaaffy",
        "src": "flaaffy.png",
    },
    "181": {
        "name": "Ampharos",
        "src": "ampharos.png",
    },
    "182": {
        "name": "Bellossom",
        "src": "bellossom.png",
    },
    "183": {
        "name": "Marill",
        "src": "marill.png",
    },
    "184": {
        "name": "Azumarill",
        "src": "azumarill.png",
    },
    "185": {
        "name": "Sudowoodo",
        "src": "sudowoodo.png",
    },
    "186": {
        "name": "Politoed",
        "src": "politoed.png",
    },
    "187": {
        "name": "Hoppip",
        "src": "hoppip.png",
    },
    "188": {
        "name": "Skiploom",
        "src": "skiploom.png",
    },
    "189": {
        "name": "Jumpluff",
        "src": "jumpluff.png",
    },
    "190": {
        "name": "Aipom",
        "src": "aipom.png",
    },
    "191": {
        "name": "Sunkern",
        "src": "sunkern.png",
    },
    "192": {
        "name": "Sunflora",
        "src": "sunflora.png",
    },
    "193": {
        "name": "Yanma",
        "src": "yanma.png",
    },
    "194": {
        "name": "Wooper",
        "src": "wooper.png",
    },
    "195": {
        "name": "Quagsire",
        "src": "quagsire.png",
    },
    "196": {
        "name": "Espeon",
        "src": "espeon.png",
    },
    "197": {
        "name": "Umbreon",
        "src": "umbreon.png",
    },
    "198": {
        "name": "Murkrow",
        "src": "murkrow.png",
    },
    "199": {
        "name": "Slowking",
        "src": "slowking.png",
    },
    "200": {
        "name": "Misdreavus",
        "src": "misdreavus.png",
    },
    "201": {
        "name": "Unown",
        "src": "unown.png",
    },
    "202": {
        "name": "Wobbuffet",
        "src": "wobbuffet.png",
    },
    "203": {
        "name": "Girafarig",
        "src": "girafarig.png",
    },
    "204": {
        "name": "Pineco",
        "src": "pineco.png",
    },
    "205": {
        "name": "Forretress",
        "src": "forretress.png",
    },
    "206": {
        "name": "Dunsparce",
        "src": "dunsparce.png",
    },
    "207": {
        "name": "Gligar",
        "src": "gligar.png",
    },
    "208": {
        "name": "Steelix",
        "src": "steelix.png",
    },
    "209": {
        "name": "Snubbull",
        "src": "snubbull.png",
    },
    "210": {
        "name": "Granbull",
        "src": "granbull.png",
    },
    "211": {
        "name": "Qwilfish",
        "src": "qwilfish.png",
    },
    "212": {
        "name": "Scizor",
        "src": "scizor.png",
    },
    "213": {
        "name": "Shuckle",
        "src": "shuckle.png",
    },
    "214": {
        "name": "Heracross",
        "src": "heracross.png",
    },
    "215": {
        "name": "Sneasel",
        "src": "sneasel.png",
    },
    "216": {
        "name": "Teddiursa",
        "src": "teddiursa.png",
    },
    "217": {
        "name": "Ursaring",
        "src": "ursaring.png",
    },
    "218": {
        "name": "Slugma",
        "src": "slugma.png",
    },
    "219": {
        "name": "Magcargo",
        "src": "magcargo.png",
    },
    "220": {
        "name": "Swinub",
        "src": "swinub.png",
    },
    "221": {
        "name": "Piloswine",
        "src": "piloswine.png",
    },
    "222": {
        "name": "Corsola",
        "src": "corsola.png",
    },
    "223": {
        "name": "Remoraid",
        "src": "remoraid.png",
    },
    "224": {
        "name": "Octillery",
        "src": "octillery.png",
    },
    "225": {
        "name": "Delibird",
        "src": "delibird.png",
    },
    "226": {
        "name": "Mantine",
        "src": "mantine.png",
    },
    "227": {
        "name": "Skarmory",
        "src": "skarmory.png",
    },
    "228": {
        "name": "Houndour",
        "src": "houndour.png",
    },
    "229": {
        "name": "Houndoom",
        "src": "houndoom.png",
    },
    "230": {
        "name": "Kingdra",
        "src": "kingdra.png",
    },
    "231": {
        "name": "Phanpy",
        "src": "phanpy.png",
    },
    "232": {
        "name": "Donphan",
        "src": "donphan.png",
    },
    "233": {
        "name": "Porygon2",
        "src": "porygon2.png",
    },
    "234": {
        "name": "Stantler",
        "src": "stantler.png",
    },
    "235": {
        "name": "Smeargle",
        "src": "smeargle.png",
    },
    "236": {
        "name": "Tyrogue",
        "src": "tyrogue.png",
    },
    "237": {
        "name": "Hitmontop",
        "src": "hitmontop.png",
    },
    "238": {
        "name": "Smoochum",
        "src": "smoochum.png",
    },
    "239": {
        "name": "Elekid",
        "src": "elekid.png",
    },
    "240": {
        "name": "Magby",
        "src": "magby.png",
    },
    "241": {
        "name": "Miltank",
        "src": "miltank.png",
    },
    "242": {
        "name": "Blissey",
        "src": "blissey.png",
    },
    "243": {
        "name": "Raikou",
        "src": "raikou.png",
    },
    "244": {
        "name": "Entei",
        "src": "entei.png",
    },
    "245": {
        "name": "Suicune",
        "src": "suicune.png",
    },
    "246": {
        "name": "Larvitar",
        "src": "larvitar.png",
    },
    "247": {
        "name": "Pupitar",
        "src": "pupitar.png",
    },
    "248": {
        "name": "Tyranitar",
        "src": "tyranitar.png",
    },
    "249": {
        "name": "Lugia",
        "src": "lugia.png",
    },
    "250": {
        "name": "Ho-oh",
        "src": "ho-oh.png",
    },
    "251": {
        "name": "Celebi",
        "src": "celebi.png",
    },
    "252": {
        "name": "Treecko",
        "src": "treecko.png",
    },
    "253": {
        "name": "Grovyle",
        "src": "grovyle.png",
    },
    "254": {
        "name": "Sceptile",
        "src": "sceptile.png",
    },
    "255": {
        "name": "Torchic",
        "src": "torchic.png",
    },
    "256": {
        "name": "Combusken",
        "src": "combusken.png",
    },
    "257": {
        "name": "Blaziken",
        "src": "blaziken.png",
    },
    "258": {
        "name": "Mudkip",
        "src": "mudkip.png",
    },
    "259": {
        "name": "Marshtomp",
        "src": "marshtomp.png",
    },
    "260": {
        "name": "Swampert",
        "src": "swampert.png",
    },
    "261": {
        "name": "Poochyena",
        "src": "poochyena.png",
    },
    "262": {
        "name": "Mightyena",
        "src": "mightyena.png",
    },
    "263": {
        "name": "Zigzagoon",
        "src": "zigzagoon.png",
    },
    "264": {
        "name": "Linoone",
        "src": "linoone.png",
    },
    "265": {
        "name": "Wurmple",
        "src": "wurmple.png",
    },
    "266": {
        "name": "Silcoon",
        "src": "silcoon.png",
    },
    "267": {
        "name": "Beautifly",
        "src": "beautifly.png",
    },
    "268": {
        "name": "Cascoon",
        "src": "cascoon.png",
    },
    "269": {
        "name": "Dustox",
        "src": "dustox.png",
    },
    "270": {
        "name": "Lotad",
        "src": "lotad.png",
    },
    "271": {
        "name": "Lombre",
        "src": "lombre.png",
    },
    "272": {
        "name": "Ludicolo",
        "src": "ludicolo.png",
    },
    "273": {
        "name": "Seedot",
        "src": "seedot.png",
    },
    "274": {
        "name": "Nuzleaf",
        "src": "nuzleaf.png",
    },
    "275": {
        "name": "Shiftry",
        "src": "shiftry.png",
    },
    "276": {
        "name": "Taillow",
        "src": "taillow.png",
    },
    "277": {
        "name": "Swellow",
        "src": "swellow.png",
    },
    "278": {
        "name": "Wingull",
        "src": "wingull.png",
    },
    "279": {
        "name": "Pelipper",
        "src": "pelipper.png",
    },
    "280": {
        "name": "Ralts",
        "src": "ralts.png",
    },
    "281": {
        "name": "Kirlia",
        "src": "kirlia.png",
    },
    "282": {
        "name": "Gardevoir",
        "src": "gardevoir.png",
    },
    "283": {
        "name": "Surskit",
        "src": "surskit.png",
    },
    "284": {
        "name": "Masquerain",
        "src": "masquerain.png",
    },
    "285": {
        "name": "Shroomish",
        "src": "shroomish.png",
    },
    "286": {
        "name": "Breloom",
        "src": "breloom.png",
    },
    "287": {
        "name": "Slakoth",
        "src": "slakoth.png",
    },
    "288": {
        "name": "Vigoroth",
        "src": "vigoroth.png",
    },
    "289": {
        "name": "Slaking",
        "src": "slaking.png",
    },
    "290": {
        "name": "Nincada",
        "src": "nincada.png",
    },
    "291": {
        "name": "Ninjask",
        "src": "ninjask.png",
    },
    "292": {
        "name": "Shedinja",
        "src": "shedinja.png",
    },
    "293": {
        "name": "Whismur",
        "src": "whismur.png",
    },
    "294": {
        "name": "Loudred",
        "src": "loudred.png",
    },
    "295": {
        "name": "Exploud",
        "src": "exploud.png",
    },
    "296": {
        "name": "Makuhita",
        "src": "makuhita.png",
    },
    "297": {
        "name": "Hariyama",
        "src": "hariyama.png",
    },
    "298": {
        "name": "Azurill",
        "src": "azurill.png",
    },
    "299": {
        "name": "Nosepass",
        "src": "nosepass.png",
    },
    "300": {
        "name": "Skitty",
        "src": "skitty.png",
    },
    "301": {
        "name": "Delcatty",
        "src": "delcatty.png",
    },
    "302": {
        "name": "Sableye",
        "src": "sableye.png",
    },
    "303": {
        "name": "Mawile",
        "src": "mawile.png",
    },
    "304": {
        "name": "Aron",
        "src": "aron.png",
    },
    "305": {
        "name": "Lairon",
        "src": "lairon.png",
    },
    "306": {
        "name": "Aggron",
        "src": "aggron.png",
    },
    "307": {
        "name": "Meditite",
        "src": "meditite.png",
    },
    "308": {
        "name": "Medicham",
        "src": "medicham.png",
    },
    "309": {
        "name": "Electrike",
        "src": "electrike.png",
    },
    "310": {
        "name": "Manectric",
        "src": "manectric.png",
    },
    "311": {
        "name": "Plusle",
        "src": "plusle.png",
    },
    "312": {
        "name": "Minun",
        "src": "minun.png",
    },
    "313": {
        "name": "Volbeat",
        "src": "volbeat.png",
    },
    "314": {
        "name": "Illumise",
        "src": "illumise.png",
    },
    "315": {
        "name": "Roselia",
        "src": "roselia.png",
    },
    "316": {
        "name": "Gulpin",
        "src": "gulpin.png",
    },
    "317": {
        "name": "Swalot",
        "src": "swalot.png",
    },
    "318": {
        "name": "Carvanha",
        "src": "carvanha.png",
    },
    "319": {
        "name": "Sharpedo",
        "src": "sharpedo.png",
    },
    "320": {
        "name": "Wailmer",
        "src": "wailmer.png",
    },
    "321": {
        "name": "Wailord",
        "src": "wailord.png",
    },
    "322": {
        "name": "Numel",
        "src": "numel.png",
    },
    "323": {
        "name": "Camerupt",
        "src": "camerupt.png",
    },
    "324": {
        "name": "Torkoal",
        "src": "torkoal.png",
    },
    "325": {
        "name": "Spoink",
        "src": "spoink.png",
    },
    "326": {
        "name": "Grumpig",
        "src": "grumpig.png",
    },
    "327": {
        "name": "Spinda",
        "src": "spinda.png",
    },
    "328": {
        "name": "Trapinch",
        "src": "trapinch.png",
    },
    "329": {
        "name": "Vibrava",
        "src": "vibrava.png",
    },
    "330": {
        "name": "Flygon",
        "src": "flygon.png",
    },
    "331": {
        "name": "Cacnea",
        "src": "cacnea.png",
    },
    "332": {
        "name": "Cacturne",
        "src": "cacturne.png",
    },
    "333": {
        "name": "Swablu",
        "src": "swablu.png",
    },
    "334": {
        "name": "Altaria",
        "src": "altaria.png",
    },
    "335": {
        "name": "Zangoose",
        "src": "zangoose.png",
    },
    "336": {
        "name": "Seviper",
        "src": "seviper.png",
    },
    "337": {
        "name": "Lunatone",
        "src": "lunatone.png",
    },
    "338": {
        "name": "Solrock",
        "src": "solrock.png",
    },
    "339": {
        "name": "Barboach",
        "src": "barboach.png",
    },
    "340": {
        "name": "Whiscash",
        "src": "whiscash.png",
    },
    "341": {
        "name": "Corphish",
        "src": "corphish.png",
    },
    "342": {
        "name": "Crawdaunt",
        "src": "crawdaunt.png",
    },
    "343": {
        "name": "Baltoy",
        "src": "baltoy.png",
    },
    "344": {
        "name": "Claydol",
        "src": "claydol.png",
    },
    "345": {
        "name": "Lileep",
        "src": "lileep.png",
    },
    "346": {
        "name": "Cradily",
        "src": "cradily.png",
    },
    "347": {
        "name": "Anorith",
        "src": "anorith.png",
    },
    "348": {
        "name": "Armaldo",
        "src": "armaldo.png",
    },
    "349": {
        "name": "Feebas",
        "src": "feebas.png",
    },
    "350": {
        "name": "Milotic",
        "src": "milotic.png",
    },
    "351": {
        "name": "Castform",
        "src": "castform.png",
    },
    "352": {
        "name": "Kecleon",
        "src": "kecleon.png",
    },
    "353": {
        "name": "Shuppet",
        "src": "shuppet.png",
    },
    "354": {
        "name": "Banette",
        "src": "banette.png",
    },
    "355": {
        "name": "Duskull",
        "src": "duskull.png",
    },
    "356": {
        "name": "Dusclops",
        "src": "dusclops.png",
    },
    "357": {
        "name": "Tropius",
        "src": "tropius.png",
    },
    "358": {
        "name": "Chimecho",
        "src": "chimecho.png",
    },
    "359": {
        "name": "Absol",
        "src": "absol.png",
    },
    "360": {
        "name": "Wynaut",
        "src": "wynaut.png",
    },
    "361": {
        "name": "Snorunt",
        "src": "snorunt.png",
    },
    "362": {
        "name": "Glalie",
        "src": "glalie.png",
    },
    "363": {
        "name": "Spheal",
        "src": "spheal.png",
    },
    "364": {
        "name": "Sealeo",
        "src": "sealeo.png",
    },
    "365": {
        "name": "Walrein",
        "src": "walrein.png",
    },
    "366": {
        "name": "Clamperl",
        "src": "clamperl.png",
    },
    "367": {
        "name": "Huntail",
        "src": "huntail.png",
    },
    "368": {
        "name": "Gorebyss",
        "src": "gorebyss.png",
    },
    "369": {
        "name": "Relicanth",
        "src": "relicanth.png",
    },
    "370": {
        "name": "Luvdisc",
        "src": "luvdisc.png",
    },
    "371": {
        "name": "Bagon",
        "src": "bagon.png",
    },
    "372": {
        "name": "Shelgon",
        "src": "shelgon.png",
    },
    "373": {
        "name": "Salamence",
        "src": "salamence.png",
    },
    "374": {
        "name": "Beldum",
        "src": "beldum.png",
    },
    "375": {
        "name": "Metang",
        "src": "metang.png",
    },
    "376": {
        "name": "Metagross",
        "src": "metagross.png",
    },
    "377": {
        "name": "Regirock",
        "src": "regirock.png",
    },
    "378": {
        "name": "Regice",
        "src": "regice.png",
    },
    "379": {
        "name": "Registeel",
        "src": "registeel.png",
    },
    "380": {
        "name": "Latias",
        "src": "latias.png",
    },
    "381": {
        "name": "Latios",
        "src": "latios.png",
    },
    "382": {
        "name": "Kyogre",
        "src": "kyogre.png",
    },
    "383": {
        "name": "Groudon",
        "src": "groudon.png",
    },
    "384": {
        "name": "Rayquaza",
        "src": "rayquaza.png",
    },
    "385": {
        "name": "Jirachi",
        "src": "jirachi.png",
    },
    "386": {
        "name": "Deoxys",
        "src": "deoxys-normal.png",
    },
    "387": {
        "name": "Turtwig",
        "src": "turtwig.png",
    },
    "388": {
        "name": "Grotle",
        "src": "grotle.png",
    },
    "389": {
        "name": "Torterra",
        "src": "torterra.png",
    },
    "390": {
        "name": "Chimchar",
        "src": "chimchar.png",
    },
    "391": {
        "name": "Monferno",
        "src": "monferno.png",
    },
    "392": {
        "name": "Infernape",
        "src": "infernape.png",
    },
    "393": {
        "name": "Piplup",
        "src": "piplup.png",
    },
    "394": {
        "name": "Prinplup",
        "src": "prinplup.png",
    },
    "395": {
        "name": "Empoleon",
        "src": "empoleon.png",
    },
    "396": {
        "name": "Starly",
        "src": "starly.png",
    },
    "397": {
        "name": "Staravia",
        "src": "staravia.png",
    },
    "398": {
        "name": "Staraptor",
        "src": "staraptor.png",
    },
    "399": {
        "name": "Bidoof",
        "src": "bidoof.png",
    },
    "400": {
        "name": "Bibarel",
        "src": "bibarel.png",
    },
    "401": {
        "name": "Kricketot",
        "src": "kricketot.png",
    },
    "402": {
        "name": "Kricketune",
        "src": "kricketune.png",
    },
    "403": {
        "name": "Shinx",
        "src": "shinx.png",
    },
    "404": {
        "name": "Luxio",
        "src": "luxio.png",
    },
    "405": {
        "name": "Luxray",
        "src": "luxray.png",
    },
    "406": {
        "name": "Budew",
        "src": "budew.png",
    },
    "407": {
        "name": "Roserade",
        "src": "roserade.png",
    },
    "408": {
        "name": "Cranidos",
        "src": "cranidos.png",
    },
    "409": {
        "name": "Rampardos",
        "src": "rampardos.png",
    },
    "410": {
        "name": "Shieldon",
        "src": "shieldon.png",
    },
    "411": {
        "name": "Bastiodon",
        "src": "bastiodon.png",
    },
    "412": {
        "name": "Burmy",
        "src": "burmy.png",
    },
    "413": {
        "name": "Wormadam",
        "src": "wormadam-plant.png",
    },
    "414": {
        "name": "Mothim",
        "src": "mothim.png",
    },
    "415": {
        "name": "Combee",
        "src": "combee.png",
    },
    "416": {
        "name": "Vespiquen",
        "src": "vespiquen.png",
    },
    "417": {
        "name": "Pachirisu",
        "src": "pachirisu.png",
    },
    "418": {
        "name": "Buizel",
        "src": "buizel.png",
    },
    "419": {
        "name": "Floatzel",
        "src": "floatzel.png",
    },
    "420": {
        "name": "Cherubi",
        "src": "cherubi.png",
    },
    "421": {
        "name": "Cherrim",
        "src": "cherrim.png",
    },
    "422": {
        "name": "Shellos",
        "src": "shellos.png",
    },
    "423": {
        "name": "Gastrodon",
        "src": "gastrodon.png",
    },
    "424": {
        "name": "Ambipom",
        "src": "ambipom.png",
    },
    "425": {
        "name": "Drifloon",
        "src": "drifloon.png",
    },
    "426": {
        "name": "Drifblim",
        "src": "drifblim.png",
    },
    "427": {
        "name": "Buneary",
        "src": "buneary.png",
    },
    "428": {
        "name": "Lopunny",
        "src": "lopunny.png",
    },
    "429": {
        "name": "Mismagius",
        "src": "mismagius.png",
    },
    "430": {
        "name": "Honchkrow",
        "src": "honchkrow.png",
    },
    "431": {
        "name": "Glameow",
        "src": "glameow.png",
    },
    "432": {
        "name": "Purugly",
        "src": "purugly.png",
    },
    "433": {
        "name": "Chingling",
        "src": "chingling.png",
    },
    "434": {
        "name": "Stunky",
        "src": "stunky.png",
    },
    "435": {
        "name": "Skuntank",
        "src": "skuntank.png",
    },
    "436": {
        "name": "Bronzor",
        "src": "bronzor.png",
    },
    "437": {
        "name": "Bronzong",
        "src": "bronzong.png",
    },
    "438": {
        "name": "Bonsly",
        "src": "bonsly.png",
    },
    "439": {
        "name": "Mime Jr.",
        "src": "mime-jr.png",
    },
    "440": {
        "name": "Happiny",
        "src": "happiny.png",
    },
    "441": {
        "name": "Chatot",
        "src": "chatot.png",
    },
    "442": {
        "name": "Spiritomb",
        "src": "spiritomb.png",
    },
    "443": {
        "name": "Gible",
        "src": "gible.png",
    },
    "444": {
        "name": "Gabite",
        "src": "gabite.png",
    },
    "445": {
        "name": "Garchomp",
        "src": "garchomp.png",
    },
    "446": {
        "name": "Munchlax",
        "src": "munchlax.png",
    },
    "447": {
        "name": "Riolu",
        "src": "riolu.png",
    },
    "448": {
        "name": "Lucario",
        "src": "lucario.png",
    },
    "449": {
        "name": "Hippopotas",
        "src": "hippopotas.png",
    },
    "450": {
        "name": "Hippowdon",
        "src": "hippowdon.png",
    },
    "451": {
        "name": "Skorupi",
        "src": "skorupi.png",
    },
    "452": {
        "name": "Drapion",
        "src": "drapion.png",
    },
    "453": {
        "name": "Croagunk",
        "src": "croagunk.png",
    },
    "454": {
        "name": "Toxicroak",
        "src": "toxicroak.png",
    },
    "455": {
        "name": "Carnivine",
        "src": "carnivine.png",
    },
    "456": {
        "name": "Finneon",
        "src": "finneon.png",
    },
    "457": {
        "name": "Lumineon",
        "src": "lumineon.png",
    },
    "458": {
        "name": "Mantyke",
        "src": "mantyke.png",
    },
    "459": {
        "name": "Snover",
        "src": "snover.png",
    },
    "460": {
        "name": "Abomasnow",
        "src": "abomasnow.png",
    },
    "461": {
        "name": "Weavile",
        "src": "weavile.png",
    },
    "462": {
        "name": "Magnezone",
        "src": "magnezone.png",
    },
    "463": {
        "name": "Lickilicky",
        "src": "lickilicky.png",
    },
    "464": {
        "name": "Rhyperior",
        "src": "rhyperior.png",
    },
    "465": {
        "name": "Tangrowth",
        "src": "tangrowth.png",
    },
    "466": {
        "name": "Electivire",
        "src": "electivire.png",
    },
    "467": {
        "name": "Magmortar",
        "src": "magmortar.png",
    },
    "468": {
        "name": "Togekiss",
        "src": "togekiss.png",
    },
    "469": {
        "name": "Yanmega",
        "src": "yanmega.png",
    },
    "470": {
        "name": "Leafeon",
        "src": "leafeon.png",
    },
    "471": {
        "name": "Glaceon",
        "src": "glaceon.png",
    },
    "472": {
        "name": "Gliscor",
        "src": "gliscor.png",
    },
    "473": {
        "name": "Mamoswine",
        "src": "mamoswine.png",
    },
    "474": {
        "name": "Porygon-Z",
        "src": "porygon-z.png",
    },
    "475": {
        "name": "Gallade",
        "src": "gallade.png",
    },
    "476": {
        "name": "Probopass",
        "src": "probopass.png",
    },
    "477": {
        "name": "Dusknoir",
        "src": "dusknoir.png",
    },
    "478": {
        "name": "Froslass",
        "src": "froslass.png",
    },
    "479": {
        "name": "Rotom",
        "src": "rotom.png",
    },
    "480": {
        "name": "Uxie",
        "src": "uxie.png",
    },
    "481": {
        "name": "Mesprit",
        "src": "mesprit.png",
    },
    "482": {
        "name": "Azelf",
        "src": "azelf.png",
    },
    "483": {
        "name": "Dialga",
        "src": "dialga.png",
    },
    "484": {
        "name": "Palkia",
        "src": "palkia.png",
    },
    "485": {
        "name": "Heatran",
        "src": "heatran.png",
    },
    "486": {
        "name": "Regigigas",
        "src": "regigigas.png",
    },
    "487": {
        "name": "Giratina",
        "src": "giratina-altered.png",
    },
    "488": {
        "name": "Cresselia",
        "src": "cresselia.png",
    },
    "489": {
        "name": "Phione",
        "src": "phione.png",
    },
    "490": {
        "name": "Manaphy",
        "src": "manaphy.png",
    },
    "491": {
        "name": "Darkrai",
        "src": "darkrai.png",
    },
    "492": {
        "name": "Shaymin",
        "src": "shaymin-land.png",
    },
    "493": {
        "name": "Arceus",
        "src": "arceus.png",
    },
    "494": {
        "name": "Victini",
        "src": "victini.png",
    },
    "495": {
        "name": "Snivy",
        "src": "snivy.png",
    },
    "496": {
        "name": "Servine",
        "src": "servine.png",
    },
    "497": {
        "name": "Serperior",
        "src": "serperior.png",
    },
    "498": {
        "name": "Tepig",
        "src": "tepig.png",
    },
    "499": {
        "name": "Pignite",
        "src": "pignite.png",
    },
    "500": {
        "name": "Emboar",
        "src": "emboar.png",
    },
    "501": {
        "name": "Oshawott",
        "src": "oshawott.png",
    },
    "502": {
        "name": "Dewott",
        "src": "dewott.png",
    },
    "503": {
        "name": "Samurott",
        "src": "samurott.png",
    },
    "504": {
        "name": "Patrat",
        "src": "patrat.png",
    },
    "505": {
        "name": "Watchog",
        "src": "watchog.png",
    },
    "506": {
        "name": "Lillipup",
        "src": "lillipup.png",
    },
    "507": {
        "name": "Herdier",
        "src": "herdier.png",
    },
    "508": {
        "name": "Stoutland",
        "src": "stoutland.png",
    },
    "509": {
        "name": "Purrloin",
        "src": "purrloin.png",
    },
    "510": {
        "name": "Liepard",
        "src": "liepard.png",
    },
    "511": {
        "name": "Pansage",
        "src": "pansage.png",
    },
    "512": {
        "name": "Simisage",
        "src": "simisage.png",
    },
    "513": {
        "name": "Pansear",
        "src": "pansear.png",
    },
    "514": {
        "name": "Simisear",
        "src": "simisear.png",
    },
    "515": {
        "name": "Panpour",
        "src": "panpour.png",
    },
    "516": {
        "name": "Simipour",
        "src": "simipour.png",
    },
    "517": {
        "name": "Munna",
        "src": "munna.png",
    },
    "518": {
        "name": "Musharna",
        "src": "musharna.png",
    },
    "519": {
        "name": "Pidove",
        "src": "pidove.png",
    },
    "520": {
        "name": "Tranquill",
        "src": "tranquill.png",
    },
    "521": {
        "name": "Unfezant",
        "src": "unfezant.png",
    },
    "522": {
        "name": "Blitzle",
        "src": "blitzle.png",
    },
    "523": {
        "name": "Zebstrika",
        "src": "zebstrika.png",
    },
    "524": {
        "name": "Roggenrola",
        "src": "roggenrola.png",
    },
    "525": {
        "name": "Boldore",
        "src": "boldore.png",
    },
    "526": {
        "name": "Gigalith",
        "src": "gigalith.png",
    },
    "527": {
        "name": "Woobat",
        "src": "woobat.png",
    },
    "528": {
        "name": "Swoobat",
        "src": "swoobat.png",
    },
    "529": {
        "name": "Drilbur",
        "src": "drilbur.png",
    },
    "530": {
        "name": "Excadrill",
        "src": "excadrill.png",
    },
    "531": {
        "name": "Audino",
        "src": "audino.png",
    },
    "532": {
        "name": "Timburr",
        "src": "timburr.png",
    },
    "533": {
        "name": "Gurdurr",
        "src": "gurdurr.png",
    },
    "534": {
        "name": "Conkeldurr",
        "src": "conkeldurr.png",
    },
    "535": {
        "name": "Tympole",
        "src": "tympole.png",
    },
    "536": {
        "name": "Palpitoad",
        "src": "palpitoad.png",
    },
    "537": {
        "name": "Seismitoad",
        "src": "seismitoad.png",
    },
    "538": {
        "name": "Throh",
        "src": "throh.png",
    },
    "539": {
        "name": "Sawk",
        "src": "sawk.png",
    },
    "540": {
        "name": "Sewaddle",
        "src": "sewaddle.png",
    },
    "541": {
        "name": "Swadloon",
        "src": "swadloon.png",
    },
    "542": {
        "name": "Leavanny",
        "src": "leavanny.png",
    },
    "543": {
        "name": "Venipede",
        "src": "venipede.png",
    },
    "544": {
        "name": "Whirlipede",
        "src": "whirlipede.png",
    },
    "545": {
        "name": "Scolipede",
        "src": "scolipede.png",
    },
    "546": {
        "name": "Cottonee",
        "src": "cottonee.png",
    },
    "547": {
        "name": "Whimsicott",
        "src": "whimsicott.png",
    },
    "548": {
        "name": "Petilil",
        "src": "petilil.png",
    },
    "549": {
        "name": "Lilligant",
        "src": "lilligant.png",
    },
    "550": {
        "name": "Basculin",
        "src": "basculin-red-striped.png",
    },
    "551": {
        "name": "Sandile",
        "src": "sandile.png",
    },
    "552": {
        "name": "Krokorok",
        "src": "krokorok.png",
    },
    "553": {
        "name": "Krookodile",
        "src": "krookodile.png",
    },
    "554": {
        "name": "Darumaka",
        "src": "darumaka.png",
    },
    "555": {
        "name": "Darmanitan",
        "src": "darmanitan-standard.png",
    },
    "556": {
        "name": "Maractus",
        "src": "maractus.png",
    },
    "557": {
        "name": "Dwebble",
        "src": "dwebble.png",
    },
    "558": {
        "name": "Crustle",
        "src": "crustle.png",
    },
    "559": {
        "name": "Scraggy",
        "src": "scraggy.png",
    },
    "560": {
        "name": "Scrafty",
        "src": "scrafty.png",
    },
    "561": {
        "name": "Sigilyph",
        "src": "sigilyph.png",
    },
    "562": {
        "name": "Yamask",
        "src": "yamask.png",
    },
    "563": {
        "name": "Cofagrigus",
        "src": "cofagrigus.png",
    },
    "564": {
        "name": "Tirtouga",
        "src": "tirtouga.png",
    },
    "565": {
        "name": "Carracosta",
        "src": "carracosta.png",
    },
    "566": {
        "name": "Archen",
        "src": "archen.png",
    },
    "567": {
        "name": "Archeops",
        "src": "archeops.png",
    },
    "568": {
        "name": "Trubbish",
        "src": "trubbish.png",
    },
    "569": {
        "name": "Garbodor",
        "src": "garbodor.png",
    },
    "570": {
        "name": "Zorua",
        "src": "zorua.png",
    },
    "571": {
        "name": "Zoroark",
        "src": "zoroark.png",
    },
    "572": {
        "name": "Minccino",
        "src": "minccino.png",
    },
    "573": {
        "name": "Cinccino",
        "src": "cinccino.png",
    },
    "574": {
        "name": "Gothita",
        "src": "gothita.png",
    },
    "575": {
        "name": "Gothorita",
        "src": "gothorita.png",
    },
    "576": {
        "name": "Gothitelle",
        "src": "gothitelle.png",
    },
    "577": {
        "name": "Solosis",
        "src": "solosis.png",
    },
    "578": {
        "name": "Duosion",
        "src": "duosion.png",
    },
    "579": {
        "name": "Reuniclus",
        "src": "reuniclus.png",
    },
    "580": {
        "name": "Ducklett",
        "src": "ducklett.png",
    },
    "581": {
        "name": "Swanna",
        "src": "swanna.png",
    },
    "582": {
        "name": "Vanillite",
        "src": "vanillite.png",
    },
    "583": {
        "name": "Vanillish",
        "src": "vanillish.png",
    },
    "584": {
        "name": "Vanilluxe",
        "src": "vanilluxe.png",
    },
    "585": {
        "name": "Deerling",
        "src": "deerling.png",
    },
    "586": {
        "name": "Sawsbuck",
        "src": "sawsbuck.png",
    },
    "587": {
        "name": "Emolga",
        "src": "emolga.png",
    },
    "588": {
        "name": "Karrablast",
        "src": "karrablast.png",
    },
    "589": {
        "name": "Escavalier",
        "src": "escavalier.png",
    },
    "590": {
        "name": "Foongus",
        "src": "foongus.png",
    },
    "591": {
        "name": "Amoonguss",
        "src": "amoonguss.png",
    },
    "592": {
        "name": "Frillish",
        "src": "frillish.png",
    },
    "593": {
        "name": "Jellicent",
        "src": "jellicent.png",
    },
    "594": {
        "name": "Alomomola",
        "src": "alomomola.png",
    },
    "595": {
        "name": "Joltik",
        "src": "joltik.png",
    },
    "596": {
        "name": "Galvantula",
        "src": "galvantula.png",
    },
    "597": {
        "name": "Ferroseed",
        "src": "ferroseed.png",
    },
    "598": {
        "name": "Ferrothorn",
        "src": "ferrothorn.png",
    },
    "599": {
        "name": "Klink",
        "src": "klink.png",
    },
    "600": {
        "name": "Klang",
        "src": "klang.png",
    },
    "601": {
        "name": "Klinklang",
        "src": "klinklang.png",
    },
    "602": {
        "name": "Tynamo",
        "src": "tynamo.png",
    },
    "603": {
        "name": "Eelektrik",
        "src": "eelektrik.png",
    },
    "604": {
        "name": "Eelektross",
        "src": "eelektross.png",
    },
    "605": {
        "name": "Elgyem",
        "src": "elgyem.png",
    },
    "606": {
        "name": "Beheeyem",
        "src": "beheeyem.png",
    },
    "607": {
        "name": "Litwick",
        "src": "litwick.png",
    },
    "608": {
        "name": "Lampent",
        "src": "lampent.png",
    },
    "609": {
        "name": "Chandelure",
        "src": "chandelure.png",
    },
    "610": {
        "name": "Axew",
        "src": "axew.png",
    },
    "611": {
        "name": "Fraxure",
        "src": "fraxure.png",
    },
    "612": {
        "name": "Haxorus",
        "src": "haxorus.png",
    },
    "613": {
        "name": "Cubchoo",
        "src": "cubchoo.png",
    },
    "614": {
        "name": "Beartic",
        "src": "beartic.png",
    },
    "615": {
        "name": "Cryogonal",
        "src": "cryogonal.png",
    },
    "616": {
        "name": "Shelmet",
        "src": "shelmet.png",
    },
    "617": {
        "name": "Accelgor",
        "src": "accelgor.png",
    },
    "618": {
        "name": "Stunfisk",
        "src": "stunfisk.png",
    },
    "619": {
        "name": "Mienfoo",
        "src": "mienfoo.png",
    },
    "620": {
        "name": "Mienshao",
        "src": "mienshao.png",
    },
    "621": {
        "name": "Druddigon",
        "src": "druddigon.png",
    },
    "622": {
        "name": "Golett",
        "src": "golett.png",
    },
    "623": {
        "name": "Golurk",
        "src": "golurk.png",
    },
    "624": {
        "name": "Pawniard",
        "src": "pawniard.png",
    },
    "625": {
        "name": "Bisharp",
        "src": "bisharp.png",
    },
    "626": {
        "name": "Bouffalant",
        "src": "bouffalant.png",
    },
    "627": {
        "name": "Rufflet",
        "src": "rufflet.png",
    },
    "628": {
        "name": "Braviary",
        "src": "braviary.png",
    },
    "629": {
        "name": "Vullaby",
        "src": "vullaby.png",
    },
    "630": {
        "name": "Mandibuzz",
        "src": "mandibuzz.png",
    },
    "631": {
        "name": "Heatmor",
        "src": "heatmor.png",
    },
    "632": {
        "name": "Durant",
        "src": "durant.png",
    },
    "633": {
        "name": "Deino",
        "src": "deino.png",
    },
    "634": {
        "name": "Zweilous",
        "src": "zweilous.png",
    },
    "635": {
        "name": "Hydreigon",
        "src": "hydreigon.png",
    },
    "636": {
        "name": "Larvesta",
        "src": "larvesta.png",
    },
    "637": {
        "name": "Volcarona",
        "src": "volcarona.png",
    },
    "638": {
        "name": "Cobalion",
        "src": "cobalion.png",
    },
    "639": {
        "name": "Terrakion",
        "src": "terrakion.png",
    },
    "640": {
        "name": "Virizion",
        "src": "virizion.png",
    },
    "641": {
        "name": "Tornadus",
        "src": "tornadus-incarnate.png",
    },
    "642": {
        "name": "Thundurus",
        "src": "thundurus-incarnate.png",
    },
    "643": {
        "name": "Reshiram",
        "src": "reshiram.png",
    },
    "644": {
        "name": "Zekrom",
        "src": "zekrom.png",
    },
    "645": {
        "name": "Landorus",
        "src": "landorus-incarnate.png",
    },
    "646": {
        "name": "Kyurem",
        "src": "kyurem.png",
    },
    "647": {
        "name": "Keldeo",
        "src": "keldeo-ordinary.png",
    },
    "648": {
        "name": "Meloetta",
        "src": "meloetta-aria.png",
    },
    "649": {
        "name": "Genesect",
        "src": "genesect.png",
    },
    "650": {
        "name": "Chespin",
        "src": "chespin.png",
    },
    "651": {
        "name": "Quilladin",
        "src": "quilladin.png",
    },
    "652": {
        "name": "Chesnaught",
        "src": "chesnaught.png",
    },
    "653": {
        "name": "Fennekin",
        "src": "fennekin.png",
    },
    "654": {
        "name": "Braixen",
        "src": "braixen.png",
    },
    "655": {
        "name": "Delphox",
        "src": "delphox.png",
    },
    "656": {
        "name": "Froakie",
        "src": "froakie.png",
    },
    "657": {
        "name": "Frogadier",
        "src": "frogadier.png",
    },
    "658": {
        "name": "Greninja",
        "src": "greninja.png",
    },
    "659": {
        "name": "Bunnelby",
        "src": "bunnelby.png",
    },
    "660": {
        "name": "Diggersby",
        "src": "diggersby.png",
    },
    "661": {
        "name": "Fletchling",
        "src": "fletchling.png",
    },
    "662": {
        "name": "Fletchinder",
        "src": "fletchinder.png",
    },
    "663": {
        "name": "Talonflame",
        "src": "talonflame.png",
    },
    "664": {
        "name": "Scatterbug",
        "src": "scatterbug.png",
    },
    "665": {
        "name": "Spewpa",
        "src": "spewpa.png",
    },
    "666": {
        "name": "Vivillon",
        "src": "vivillon.png",
    },
    "667": {
        "name": "Litleo",
        "src": "litleo.png",
    },
    "668": {
        "name": "Pyroar",
        "src": "pyroar.png",
    },
    "669": {
        "name": "Flabébé",
        "src": "flabebe.png",
    },
    "670": {
        "name": "Floette",
        "src": "floette.png",
    },
    "671": {
        "name": "Florges",
        "src": "florges.png",
    },
    "672": {
        "name": "Skiddo",
        "src": "skiddo.png",
    },
    "673": {
        "name": "Gogoat",
        "src": "gogoat.png",
    },
    "674": {
        "name": "Pancham",
        "src": "pancham.png",
    },
    "675": {
        "name": "Pangoro",
        "src": "pangoro.png",
    },
    "676": {
        "name": "Furfrou",
        "src": "furfrou.png",
    },
    "677": {
        "name": "Espurr",
        "src": "espurr.png",
    },
    "678": {
        "name": "Meowstic",
        "src": "meowstic-male.png",
    },
    "679": {
        "name": "Honedge",
        "src": "honedge.png",
    },
    "680": {
        "name": "Doublade",
        "src": "doublade.png",
    },
    "681": {
        "name": "Aegislash",
        "src": "aegislash-shield.png",
    },
    "682": {
        "name": "Spritzee",
        "src": "spritzee.png",
    },
    "683": {
        "name": "Aromatisse",
        "src": "aromatisse.png",
    },
    "684": {
        "name": "Swirlix",
        "src": "swirlix.png",
    },
    "685": {
        "name": "Slurpuff",
        "src": "slurpuff.png",
    },
    "686": {
        "name": "Inkay",
        "src": "inkay.png",
    },
    "687": {
        "name": "Malamar",
        "src": "malamar.png",
    },
    "688": {
        "name": "Binacle",
        "src": "binacle.png",
    },
    "689": {
        "name": "Barbaracle",
        "src": "barbaracle.png",
    },
    "690": {
        "name": "Skrelp",
        "src": "skrelp.png",
    },
    "691": {
        "name": "Dragalge",
        "src": "dragalge.png",
    },
    "692": {
        "name": "Clauncher",
        "src": "clauncher.png",
    },
    "693": {
        "name": "Clawitzer",
        "src": "clawitzer.png",
    },
    "694": {
        "name": "Helioptile",
        "src": "helioptile.png",
    },
    "695": {
        "name": "Heliolisk",
        "src": "heliolisk.png",
    },
    "696": {
        "name": "Tyrunt",
        "src": "tyrunt.png",
    },
    "697": {
        "name": "Tyrantrum",
        "src": "tyrantrum.png",
    },
    "698": {
        "name": "Amaura",
        "src": "amaura.png",
    },
    "699": {
        "name": "Aurorus",
        "src": "aurorus.png",
    },
    "700": {
        "name": "Sylveon",
        "src": "sylveon.png",
    },
    "701": {
        "name": "Hawlucha",
        "src": "hawlucha.png",
    },
    "702": {
        "name": "Dedenne",
        "src": "dedenne.png",
    },
    "703": {
        "name": "Carbink",
        "src": "carbink.png",
    },
    "704": {
        "name": "Goomy",
        "src": "goomy.png",
    },
    "705": {
        "name": "Sliggoo",
        "src": "sliggoo.png",
    },
    "706": {
        "name": "Goodra",
        "src": "goodra.png",
    },
    "707": {
        "name": "Klefki",
        "src": "klefki.png",
    },
    "708": {
        "name": "Phantump",
        "src": "phantump.png",
    },
    "709": {
        "name": "Trevenant",
        "src": "trevenant.png",
    },
    "710": {
        "name": "Pumpkaboo",
        "src": "pumpkaboo-average.png",
    },
    "711": {
        "name": "Gourgeist",
        "src": "gourgeist-average.png",
    },
    "712": {
        "name": "Bergmite",
        "src": "bergmite.png",
    },
    "713": {
        "name": "Avalugg",
        "src": "avalugg.png",
    },
    "714": {
        "name": "Noibat",
        "src": "noibat.png",
    },
    "715": {
        "name": "Noivern",
        "src": "noivern.png",
    },
    "716": {
        "name": "Xerneas",
        "src": "xerneas.png",
    },
    "717": {
        "name": "Yveltal",
        "src": "yveltal.png",
    },
    "718": {
        "name": "Zygarde",
        "src": "zygarde-50.png",
    },
    "719": {
        "name": "Diancie",
        "src": "diancie.png",
    },
    "720": {
        "name": "Hoopa",
        "src": "hoopa-confined.png",
    },
    "721": {
        "name": "Volcanion",
        "src": "volcanion.png",
    },
    "722": {
        "name": "Rowlet",
        "src": "rowlet.png",
    },
    "723": {
        "name": "Dartrix",
        "src": "dartrix.png",
    },
    "724": {
        "name": "Decidueye",
        "src": "decidueye.png",
    },
    "725": {
        "name": "Litten",
        "src": "litten.png",
    },
    "726": {
        "name": "Torracat",
        "src": "torracat.png",
    },
    "727": {
        "name": "Incineroar",
        "src": "incineroar.png",
    },
    "728": {
        "name": "Popplio",
        "src": "popplio.png",
    },
    "729": {
        "name": "Brionne",
        "src": "brionne.png",
    },
    "730": {
        "name": "Primarina",
        "src": "primarina.png",
    },
    "731": {
        "name": "Pikipek",
        "src": "pikipek.png",
    },
    "732": {
        "name": "Trumbeak",
        "src": "trumbeak.png",
    },
    "733": {
        "name": "Toucannon",
        "src": "toucannon.png",
    },
    "734": {
        "name": "Yungoos",
        "src": "yungoos.png",
    },
    "735": {
        "name": "Gumshoos",
        "src": "gumshoos.png",
    },
    "736": {
        "name": "Grubbin",
        "src": "grubbin.png",
    },
    "737": {
        "name": "Charjabug",
        "src": "charjabug.png",
    },
    "738": {
        "name": "Vikavolt",
        "src": "vikavolt.png",
    },
    "739": {
        "name": "Crabrawler",
        "src": "crabrawler.png",
    },
    "740": {
        "name": "Crabominable",
        "src": "crabominable.png",
    },
    "741": {
        "name": "Oricorio",
        "src": "oricorio-baile.png",
    },
    "742": {
        "name": "Cutiefly",
        "src": "cutiefly.png",
    },
    "743": {
        "name": "Ribombee",
        "src": "ribombee.png",
    },
    "744": {
        "name": "Rockruff",
        "src": "rockruff.png",
    },
    "745": {
        "name": "Lycanroc",
        "src": "lycanroc-midday.png",
    },
    "746": {
        "name": "Wishiwashi",
        "src": "wishiwashi-solo.png",
    },
    "747": {
        "name": "Mareanie",
        "src": "mareanie.png",
    },
    "748": {
        "name": "Toxapex",
        "src": "toxapex.png",
    },
    "749": {
        "name": "Mudbray",
        "src": "mudbray.png",
    },
    "750": {
        "name": "Mudsdale",
        "src": "mudsdale.png",
    },
    "751": {
        "name": "Dewpider",
        "src": "dewpider.png",
    },
    "752": {
        "name": "Araquanid",
        "src": "araquanid.png",
    },
    "753": {
        "name": "Fomantis",
        "src": "fomantis.png",
    },
    "754": {
        "name": "Lurantis",
        "src": "lurantis.png",
    },
    "755": {
        "name": "Morelull",
        "src": "morelull.png",
    },
    "756": {
        "name": "Shiinotic",
        "src": "shiinotic.png",
    },
    "757": {
        "name": "Salandit",
        "src": "salandit.png",
    },
    "758": {
        "name": "Salazzle",
        "src": "salazzle.png",
    },
    "759": {
        "name": "Stufful",
        "src": "stufful.png",
    },
    "760": {
        "name": "Bewear",
        "src": "bewear.png",
    },
    "761": {
        "name": "Bounsweet",
        "src": "bounsweet.png",
    },
    "762": {
        "name": "Steenee",
        "src": "steenee.png",
    },
    "763": {
        "name": "Tsareena",
        "src": "tsareena.png",
    },
    "764": {
        "name": "Comfey",
        "src": "comfey.png",
    },
    "765": {
        "name": "Oranguru",
        "src": "oranguru.png",
    },
    "766": {
        "name": "Passimian",
        "src": "passimian.png",
    },
    "767": {
        "name": "Wimpod",
        "src": "wimpod.png",
    },
    "768": {
        "name": "Golisopod",
        "src": "golisopod.png",
    },
    "769": {
        "name": "Sandygast",
        "src": "sandygast.png",
    },
    "770": {
        "name": "Palossand",
        "src": "palossand.png",
    },
    "771": {
        "name": "Pyukumuku",
        "src": "pyukumuku.png",
    },
    "772": {
        "name": "Type: Null",
        "src": "type-null.png",
    },
    "773": {
        "name": "Silvally",
        "src": "silvally.png",
    },
    "774": {
        "name": "Minior",
        "src": "minior-meteor.png",
    },
    "775": {
        "name": "Komala",
        "src": "komala.png",
    },
    "776": {
        "name": "Turtonator",
        "src": "turtonator.png",
    },
    "777": {
        "name": "Togedemaru",
        "src": "togedemaru.png",
    },
    "778": {
        "name": "Mimikyu",
        "src": "mimikyu.png",
    },
    "779": {
        "name": "Bruxish",
        "src": "bruxish.png",
    },
    "780": {
        "name": "Drampa",
        "src": "drampa.png",
    },
    "781": {
        "name": "Dhelmise",
        "src": "dhelmise.png",
    },
    "782": {
        "name": "Jangmo-o",
        "src": "jangmo-o.png",
    },
    "783": {
        "name": "Hakamo-o",
        "src": "hakamo-o.png",
    },
    "784": {
        "name": "Kommo-o",
        "src": "kommo-o.png",
    },
    "785": {
        "name": "Tapu Koko",
        "src": "tapu-koko.png",
    },
    "786": {
        "name": "Tapu Lele",
        "src": "tapu-lele.png",
    },
    "787": {
        "name": "Tapu Bulu",
        "src": "tapu-bulu.png",
    },
    "788": {
        "name": "Tapu Fini",
        "src": "tapu-fini.png",
    },
    "789": {
        "name": "Cosmog",
        "src": "cosmog.png",
    },
    "790": {
        "name": "Cosmoem",
        "src": "cosmoem.png",
    },
    "791": {
        "name": "Solgaleo",
        "src": "solgaleo.png",
    },
    "792": {
        "name": "Lunala",
        "src": "lunala.png",
    },
    "793": {
        "name": "Nihilego",
        "src": "nihilego.png",
    },
    "794": {
        "name": "Buzzwole",
        "src": "buzzwole.png",
    },
    "795": {
        "name": "Pheromosa",
        "src": "pheromosa.png",
    },
    "796": {
        "name": "Xurkitree",
        "src": "xurkitree.png",
    },
    "797": {
        "name": "Celesteela",
        "src": "celesteela.png",
    },
    "798": {
        "name": "Kartana",
        "src": "kartana.png",
    },
    "799": {
        "name": "Guzzlord",
        "src": "guzzlord.png",
    },
    "800": {
        "name": "Necrozma",
        "src": "necrozma.png",
    },
    "801": {
        "name": "Magearna",
        "src": "magearna.png",
    },
    "802": {
        "name": "Marshadow",
        "src": "marshadow.png",
    },
    "803": {
        "name": "Poipole",
        "src": "poipole.png",
    },
    "804": {
        "name": "Naganadel",
        "src": "naganadel.png",
    },
    "805": {
        "name": "Stakataka",
        "src": "stakataka.png",
    },
    "806": {
        "name": "Blacephalon",
        "src": "blacephalon.png",
    },
    "807": {
        "name": "Zeraora",
        "src": "zeraora.png",
    },
    "808": {
        "name": "Meltan",
        "src": "meltan.png",
    },
    "809": {
        "name": "Melmetal",
        "src": "melmetal.png",
    },
    "810": {
        "name": "Grookey",
        "src": "grookey.png",
    },
    "811": {
        "name": "Thwackey",
        "src": "thwackey.png",
    },
    "812": {
        "name": "Rillaboom",
        "src": "rillaboom.png",
    },
    "813": {
        "name": "Scorbunny",
        "src": "scorbunny.png",
    },
    "814": {
        "name": "Raboot",
        "src": "raboot.png",
    },
    "815": {
        "name": "Cinderace",
        "src": "cinderace.png",
    },
    "816": {
        "name": "Sobble",
        "src": "sobble.png",
    },
    "817": {
        "name": "Drizzile",
        "src": "drizzile.png",
    },
    "818": {
        "name": "Inteleon",
        "src": "inteleon.png",
    },
    "819": {
        "name": "Skwovet",
        "src": "skwovet.png",
    },
    "820": {
        "name": "Greedent",
        "src": "greedent.png",
    },
    "821": {
        "name": "Rookidee",
        "src": "rookidee.png",
    },
    "822": {
        "name": "Corvisquire",
        "src": "corvisquire.png",
    },
    "823": {
        "name": "Corviknight",
        "src": "corviknight.png",
    },
    "824": {
        "name": "Blipbug",
        "src": "blipbug.png",
    },
    "825": {
        "name": "Dottler",
        "src": "dottler.png",
    },
    "826": {
        "name": "Orbeetle",
        "src": "orbeetle.png",
    },
    "827": {
        "name": "Nickit",
        "src": "nickit.png",
    },
    "828": {
        "name": "Thievul",
        "src": "thievul.png",
    },
    "829": {
        "name": "Gossifleur",
        "src": "gossifleur.png",
    },
    "830": {
        "name": "Eldegoss",
        "src": "eldegoss.png",
    },
    "831": {
        "name": "Wooloo",
        "src": "wooloo.png",
    },
    "832": {
        "name": "Dubwool",
        "src": "dubwool.png",
    },
    "833": {
        "name": "Chewtle",
        "src": "chewtle.png",
    },
    "834": {
        "name": "Drednaw",
        "src": "drednaw.png",
    },
    "835": {
        "name": "Yamper",
        "src": "yamper.png",
    },
    "836": {
        "name": "Boltund",
        "src": "boltund.png",
    },
    "837": {
        "name": "Rolycoly",
        "src": "rolycoly.png",
    },
    "838": {
        "name": "Carkol",
        "src": "carkol.png",
    },
    "839": {
        "name": "Coalossal",
        "src": "coalossal.png",
    },
    "840": {
        "name": "Applin",
        "src": "applin.png",
    },
    "841": {
        "name": "Flapple",
        "src": "flapple.png",
    },
    "842": {
        "name": "Appletun",
        "src": "appletun.png",
    },
    "843": {
        "name": "Silicobra",
        "src": "silicobra.png",
    },
    "844": {
        "name": "Sandaconda",
        "src": "sandaconda.png",
    },
    "845": {
        "name": "Cramorant",
        "src": "cramorant.png",
    },
    "846": {
        "name": "Arrokuda",
        "src": "arrokuda.png",
    },
    "847": {
        "name": "Barraskewda",
        "src": "barraskewda.png",
    },
    "848": {
        "name": "Toxel",
        "src": "toxel.png",
    },
    "849": {
        "name": "Toxtricity",
        "src": "toxtricity-low-key.png",
    },
    "850": {
        "name": "Sizzlipede",
        "src": "sizzlipede.png",
    },
    "851": {
        "name": "Centiskorch",
        "src": "centiskorch.png",
    },
    "852": {
        "name": "Clobbopus",
        "src": "clobbopus.png",
    },
    "853": {
        "name": "Grapploct",
        "src": "grapploct.png",
    },
    "854": {
        "name": "Sinistea",
        "src": "sinistea.png",
    },
    "855": {
        "name": "Polteageist",
        "src": "polteageist.png",
    },
    "856": {
        "name": "Hatenna",
        "src": "hatenna.png",
    },
    "857": {
        "name": "Hattrem",
        "src": "hattrem.png",
    },
    "858": {
        "name": "Hatterene",
        "src": "hatterene.png",
    },
    "859": {
        "name": "Impidimp",
        "src": "impidimp.png",
    },
    "860": {
        "name": "Morgrem",
        "src": "morgrem.png",
    },
    "861": {
        "name": "Grimmsnarl",
        "src": "grimmsnarl.png",
    },
    "862": {
        "name": "Obstagoon",
        "src": "obstagoon.png",
    },
    "863": {
        "name": "Perrserker",
        "src": "perrserker.png",
    },
    "864": {
        "name": "Cursola",
        "src": "cursola.png",
    },
    "865": {
        "name": "Sirfetch'd",
        "src": "sirfetchd.png",
    },
    "866": {
        "name": "Mr. Rime",
        "src": "mr-rime.png",
    },
    "867": {
        "name": "Runerigus",
        "src": "runerigus.png",
    },
    "868": {
        "name": "Milcery",
        "src": "milcery.png",
    },
    "869": {
        "name": "Alcremie",
        "src": "alcremie.png",
    },
    "870": {
        "name": "Falinks",
        "src": "falinks.png",
    },
    "871": {
        "name": "Pincurchin",
        "src": "pincurchin.png",
    },
    "872": {
        "name": "Snom",
        "src": "snom.png",
    },
    "873": {
        "name": "Frosmoth",
        "src": "frosmoth.png",
    },
    "874": {
        "name": "Stonjourner",
        "src": "stonjourner.png",
    },
    "875": {
        "name": "Eiscue",
        "src": "eiscue-ice.png",
    },
    "876": {
        "name": "Indeedee",
        "src": "indeedee-male.png",
    },
    "877": {
        "name": "Morpeko",
        "src": "morpeko-full-belly.png",
    },
    "878": {
        "name": "Cufant",
        "src": "cufant.png",
    },
    "879": {
        "name": "Copperajah",
        "src": "copperajah.png",
    },
    "880": {
        "name": "Dracozolt",
        "src": "dracozolt.png",
    },
    "881": {
        "name": "Arctozolt",
        "src": "arctozolt.png",
    },
    "882": {
        "name": "Dracovish",
        "src": "dracovish.png",
    },
    "883": {
        "name": "Arctovish",
        "src": "arctovish.png",
    },
    "884": {
        "name": "Duraludon",
        "src": "duraludon.png",
    },
    "885": {
        "name": "Dreepy",
        "src": "dreepy.png",
    },
    "886": {
        "name": "Drakloak",
        "src": "drakloak.png",
    },
    "887": {
        "name": "Dragapult",
        "src": "dragapult.png",
    },
    "888": {
        "name": "Zacian",
        "src": "zacian-crowned.png",
    },
    "889": {
        "name": "Zamazenta",
        "src": "zamazenta-crowned.png",
    },
    "890": {
        "name": "Eternatus",
        "src": "eternatus.png",
    },
    "891": {
        "name": "Kubfu",
        "src": "kubfu.png",
    },
    "892": {
        "name": "Urshifu",
        "src": "urshifu-single-strike.png",
    },
    "893": {
        "name": "Zarude",
        "src": "zarude.png",
    },
    "894": {
        "name": "Regieleki",
        "src": "regieleki.png",
    },
    "895": {
        "name": "Regidrago",
        "src": "regidrago.png",
    },
    "896": {
        "name": "Glastrier",
        "src": "glastrier.png",
    },
    "897": {
        "name": "Spectrier",
        "src": "spectrier.png",
    },
    "898": {
        "name": "Calyrex",
        "src": "calyrex.png",
    },
}

cache = {}


def read_one(id):
    if id in cache:
        print("cache")
        return cache[id]
    if id in POKEMONS:
        name = POKEMONS[id].get("name")
        src = POKEMONS[id].get("src")
        res = requests.get(
            "https://img.pokemondb.net/sprites/home/normal/" + src, stream=True
        ).raw
        image_read = res.read()

        original = str(base64.b64encode(image_read), encoding="utf-8")

        image = np.asarray(bytearray(image_read), dtype="uint8")

        src = cv2.imdecode(image, cv2.IMREAD_UNCHANGED)

        # make mask of where the transparent bits are
        trans_mask = src[:, :, 3] == 0

        # replace areas of transparency with white and not transparent
        src[trans_mask] = [255, 255, 255, 255]

        # # new image with no transparency
        no_alpha = cv2.cvtColor(src, cv2.COLOR_BGRA2GRAY)

        _, im_th = cv2.threshold(no_alpha, 240, 255, cv2.THRESH_BINARY)
        # _, buffer = cv2.imencode(".png", im_th)
        
        tmp = cv2.cvtColor(src, cv2.COLOR_BGRA2GRAY)
        # Applying thresholding technique 
        _, alpha = cv2.threshold(tmp, 240, 255, cv2.THRESH_BINARY) 

        # Using cv2.split() to split channels  
        # of coloured image 
        src[trans_mask] = [False, False, False, False]
        b, g, r, a = cv2.split(src) 

        # Making list of Red, Green, Blue 
        # Channels and alpha 
        rgba = [alpha, alpha, alpha, a] 

        # Using cv2.merge() to merge rgba 
        # into a coloured/multi-channeled image 
        dst = cv2.merge(rgba, 4) 
        _, buffer = cv2.imencode(".png", dst)
        
        silhouette = str(base64.b64encode(buffer), encoding="utf-8")

        pokemon = {
            "name": name,
            "original": original,
            "silhouette": silhouette,
        }
        cache[id] = pokemon
        return pokemon
    else:
        abort(404, f"Pokémon with Pokédex number {id} not found")
