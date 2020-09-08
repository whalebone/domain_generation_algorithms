from .banjori.dga import dga as banjouri
from .bazarbackdoor.dga import dga as bazarbackdoor #current date
from .chinad.dga import dga as chinad #current date
from .corebot.dga import dga as corebot #date
from .fobber.dga import dga as fobber #[1,2]
from .fosniw.dga import dga as fosniw #["winsoft", "koreasys"]
from .gozi.dga import dga as gozi #current date, ['luther', 'rfc4343', 'nasa', ]
from .kraken.v1.dga_v1 import get_domains as krakenv1 #['a','b']
from .kraken.v2.dga_v2 import get_domains as krakenv2 #current date, [1, 2], ['a','b']
from .locky.dgav2 import dga as lockv2 #date, range(1,8)
from .locky.dgav3 import dga as lockv3 #date, range(1,21)
from .monerodownloader.dga import dga as monerodownloader #date
from .murofet.v1.dga import dga as murofetv1 #date
from .murofet.v2.dga import dga as murofetv2 #date, [D6D7A4BE, DEADC2DE, D6D7A4B1]
from .murofet.v3.dga import dga as murofetv3 #date
from .mydoom.dga import dga as mydoom #date, "0xFA8", number of domaisn
from .necurs.dga import generate_necurs_domain as necursv1 #sequence number (2048), 9, date
from .necurs.dga_different_params import generate_necurs_domain as necursv2 #sequence number (2048), 9, date
from .newgoz.dga import create_domain as newgoz #sequence number (1000?), date
from .nymaim.dga import dga as nymainv1 #date
from .nymaim2.dga import dga as nymainv2 #date
from .padcrypt.dga import dga as padcrypt #date, ["2.2.86.1", "2.2.97.0"]
from .pizd.dga import pizd #date, number of domains(85))
from .proslikefan.dga import dga as proskelifan #date, [prospect, OK], ["eu", "biz", "se", "info", "com", "net", "org", "ru", "in", "name"]
from .pushdo.dga import generate_domains as pushdo #date, [kz_v1, com_v1, kz_v2]
from .pykspa.precursor.dga import generate_domains as pykspa_precursor #date, number of doamins(5000)
from .pykspa.improved.dga import generate_domains as pykspa_improved #date, number of domains(10), 1
from .qadars.dga import dga as qadars #date, ["89f5", "4449", "E1F1", "E1F2", "E08A", "E1F5"],
from .qakbot.dga import dga as qakbot #date, whole ["com", "net", "org", "info", "biz", "org"], number of domains(5000), False, [0,1]
from .qsnatch.dga_a import dga as qsnatch_a # date
from .qsnatch.dga_b import dga as qsnatch_b #date
from .ramdo.dga import dga as ramdo #0xD5FFF, range(20)
from .ramnit.dga import get_domains as ramnit #["16647BB4", "E7392D18", "C129388E", "E706B455", "DC485593", "EF214BBF", "28488EEA", "4BFCBC6A", "79159C10", "92F4BE35", "1CCEC41C", "0C5787AE2", "0FCFFD9E9", "75EA95C2", "8A0AEC7D", "1DF640A8", "14DF29DD", "8222270B", "55536A85", "5C39E467", "D2B3C361", "F318D47D", "231D9480", "13317EAC", "89547381", "6C36D41D", "52278648"] ,number of domains ,None
from .ranbyus.september.ranbyus_reloaded import dga as ranbyus #date, ["0F0D5BFA", "F2C72B14", "AE8714BE", "CE7F8514", "572473BB", "17794CF1", "C0E32524", "7CB7966E", "9F90C9E7", "8FB8879B", "E981684B"]
from .reconyc.dga import dga as reconyc
from .shiotob.dga import get_next_domain as shiotob #number of domains
from .simda.dga import dga as simba
from .sisron.dga import generate_domains as sisron #nubmer of domains
from .suppobox.dga import generate_domains as suppobox #None, [1,2,3]
from .symmi.dga import dga as symmi #date, ".ddns.net", nr of domains
from .tempedreve.dga import dga as tempedreve #date
from .tinba.dga import generate_domains as tinba
from .unknown_malware.dga import dga as unknown # ["sn", "al"]
from .unnamed_javascript_dga import dga as uknown_js #OK, date
from .vawtrak.dga3 import dga as vawtrak_v3 #int(args.seed, 16) -> {'874c49', '3cdca1'}, number of domains
from .vawtrak.dga2 import dga as vawtrak_v2 #int(args.seed, 16) -> {'0x5542b2', '0x5884c3c4'}, number of domains
from .zloader.dga import dga as zloader #date, ["q23Cud3xsNf3","41997b4a729e1a0175208305170752dd", "kZieCw23gffpe43Sd",  "Ts72YjsjO5TghE6m"], nr of domains

