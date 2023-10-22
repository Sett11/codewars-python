from re import sub,search


def doubles(s):
    s=sub(r'(.)\1+',lambda e:e.group()[0] if len(e.group())&1 else '',s)
    return s if not search(r'(.)\1+',s) else doubles(s)


print(doubles('abcda'))
print(doubles('xxcmmmmnhhhukkktwwwwuzzzzjoogmmmdccbssssliiiiweeeejllgzzsvvvvrjjjjjhgggggiwwwpyynpppibbbbbouuuuuvppppavvvvvwcceyyvhhnuuyzzzznwwwhggrgggzzzzzzxyyysffffcnnnnnabbbbhdddsrrxjjjujjcggggnccccfoobmmeuuulrrrrroxxxsssssfuudpppmiiassssswuuvbbbmiiewwwwwxgggeuuuqrrryllllullllnnnnnfaalqqqqgzzhooooocqqqtbbbbbmffffftrrrrwqqqnvvvqrrrmwwwwwgssssszmmmmmmzzzzzyxxxxxhgggihhhiyyyscccvqqqmddddwggggmllpooiaaaaavccccclbbbbqooooeppppprrrhhhhhdkkdnnnnnptttoovjjjjlgggggmmmcuuuwaaaazeeelsssssiiiiijttyppppggzeeenppppfnnnnwssssclllllhiiiiibrrrrrvhhhrmmmhzzzznhhqssswllllflllllnggggwqqqqvwwmjjjjueezuunvvvktttttqvvkaaaancccyhhjccccckuuuuudllltrrrrzrrrrwzzzsyyygqqqqsyyyffffffgjjtddjwwwpjjsqqqqdwwwxrrrrrljjjgbbbbgggceeeeyqqgooooouhhhwkkkkkyjjjjbwwhuupoootcccccrbbbbyssssqmmelllkiiiyuuutttekkkkalllllivvvhyyyysaazlllllpuuuuujnnnssssrwwwmfffffgrrrnuusxxxxxpyyyojjcjjjjjejjjjjjccovvvvveddddghhhxjjjjbxxxxxshhhsoooohhhhhxtttttskkkkkfbbbbvpppjxxxxpppppyxxxxxtaaaopppppokkkkezzmgggjddddpssssswffrlllllmaaayttttfnnekkojjfooooodddddhxxxxxzsssdssvjjjjvddddmllllnhhhhhpppppzllllgkkkzyyydrrrrogggggwzzzzhjjwcccknnnnnunnntssbggtkkaooooojnnnntxxxaeeuzzzyllexxazzzzzjqqjooooejjjuzzzzetttttyttttaqqqqoccpzzzivvvviiiiidlllxuuuuumpppnooooopfffffrfffflmmmcaaaaaoccccczrrrlxxxxhggggerrrgzzffffffegggguyyndddprrxggxvvzlllllmdddddyhhcbbsssssatttprrappthhhiggggsqqqqxsssommmmmynnnippwzzzzmyyyycttteuuuuucwwwwgwwwrgggtkkkkkmvvvvvgqqqqsyyyoppgqqqqqdmmmoeeevttttefffthhhalllllkttattwddrvvvvvibbbbbqaaaareemjjjjzzefffopppgeeevaauxxxxxxffffpeeevnnnnphhhhhkbbbmffffckkkkdccodddduzzzzrwwwszzzeuuuuupzzzzzjvvvddddtxxxymmmqiiiiixnnezzzzzutttmggzeemrrrrzwwwwbaaittthbbbbjfffrlllllvllwggxaaaaaxjjjjcssgxxxxwwwmaaaaaijjjjjhnnnnwuuuupnnddddddjuuuhiiinyyykuuuuguuuuskkkcxxxxbzzzzngggottooooogiiiiipbbdmmmcuuuuktttppppppdaaekkknookuuuurkktssssswddddduvvrllwxxtiijgggggdrrrrrviiiiidgggqdddddygggggqaarddgtttthppogggeeeeeerdddddmtttttuzzzzzohhhqiiiiyhhhhorrrrdeelssssibbbdccevvvvvlyyyyeooohwwwwwqeeeebccqsssrlllllnnnnnnrcccccbffffwwwwwwcpppppniitaaauvvvveffgmmmeeeeeeraaaagnnnnnwqqqxjjjjqbbbbbacckiiimbbbbykkvddddpzzummyffonneaavccccrwwwwwwxxxxxchhhmppallllzmmohhjccctnnnnyzzzzjrrfxxxxrhhhhjzznllllossssspwwwvfffuoooooruuhjjjjziiiiiwjjjjbwwwwwlrrrrowwwmkkkkoxxxxnxxxxxgdddddauuummfddddxooocfffopppcmmbkkkkjjjjjeeeelllsggoiiiujjjjjjnnnnncpppxllllnnqjjjeeebdddddcqqassbwwwwixxucccccdeeewmmmmmkgggarrqwwwwqfffkvvvviyycyyszzzzzivvvvvgxxxqzzzullhddbooooohgggggtttttbbbbbbfsssgjjjjjtwwwwbxxxxxmjjjjuqqqqqnbbeoooxyyywffffiwwwwwepppppshhhtdddskkkkntttdooouffffjtttttunnnnnoffflyyysmmyggggpllseeeeeiaaaqkkkkvggggyiiiiiocccccnggbffffzrrrbooooonooouzzzrqqqqqqkkkvdddddbggggkkkwaaacjjjjepppppevvvvdxxxxcooognnzpphffffswwyrrrrccceaarffwzzzzzqzzzzzyyyhbbbgnnnnpvvvvvwsssssymmmmshhhhhzeeefwwauudvvvvvmzzzzzvwwwwwwrrrrwqqqqqpggggghxxxxxhqqqqyjjjiccckdddxgggqgggggwkkkijjjjbaaaaalbbbbbdhhhhfxxxxyoooowddddkdddddrcccccfcccccvqqqqpiiiiigwwwevvxffffyfffvddpuuuuckkrzzzzpqqqqqriiiicqqqqqjvvvqggvhhjhhhhhwyyyyyreerwwwwwlbbbucccvqqqwiiipkkknfffffhmmjttttrrrrrrfiiirmmmmkiiiiitbbbbbjttceeemeeeekddsoooooljjixxxxikkkesssrcccaaaaaxllllljnnnnnysssyaaaawaaezzzjbbbbrooooouggfssfmmmmwvvvvsjjjjvmmmmmymmdaaaaatttttpbbbbzmmmvvvihhhhhzttttyggfqqqeyyummmmmtnnnqffffffxxxoyynrrrrqaaaajuuuuuykkkzzzzzrhhzvvvattxuuuuuolllllyaaaaaeeeeednnnnnxvvuuucnnnnnlhhcbbbbpvvvvcuuuuunbbmkkxoomgggwbbbbzffkwwwqrrrrrczzzzzoeeeeelssssseooolqqqqlyyhrrrrywwwwnvvvyoooksssspzzzzzzwwwwqzzzzzbsssssappaqqqxgggggxjjjjemmmnggguiiimvvvyffffsffffxqqqqqglllhffffzqqqkkcyyyyyfvvvvisssseqqqqjhhhhnjjjjpppfwwwwappppprrrrkpprnnnuzzzjxxxwggggfqqqqtiiiinmmkuuuziiiiallltbbbbbsxxxxxlzzcuuuuojjjjjvyyyykkkkoaaaaaaggztttttecccccovvvvurrrrkdddwdddddjdddruuuuujqqjyyeaaahmmmdoooooqmmmmmpcccvnnlccccuqqqhzzzzswwovvvwjjjjeoooovrrrrrfmmffffffwrrrwrrrrikkekkkmffffrfffdlluvvvueelbbammmmmallllzqqqjhhhhkffffajjcllllpzziuupaazddrrrrrkrrrrdfffffbhhhbrrrjffyssyddeiiiiydddddtoojfffcbbbbmdddiyyyksssssxvvvvvpwwwdiiiteeeeenxxkffffzjjjjeppppzttdjjjjeiiwiiiihppppzkksqqqqqfxxxxxtaaapuuuuryyykvvgkkkkkxxxbiiiiiytttkaaaavaaziiiigbbbhwwyssssfaasrrrriiibhhhhhgrrrvzzzztssssuaaaoddddzaaaeaaaaecccyccviiikrrrrebbbbbxzzzswwwwpwwwucccccxeebrrrrrtppppeaaaavhhhhhwaaaapwwwwzuuuusffaaaesssssrccujjjjjpiihvvpjjjjjmnnckkkcfffdyyyyyfxxwiiiiijiienneyyyyrryjjkqqqzvvvvaiiirnnnlwwwwwsllllehhhnmmfccccrzzzzzazzlzzzzceeyiiielllbppppqqqqqqciiiifzzzzyffffissejjzooooodlllllwcccqttttfzzvgggggntttlsssspmmmmacccxlllljttfvvvvzbbbzllllpwwwwgwwwwwjooynnnntffsrrwaaaaaawwwwwmnnnnwjjjjimmmnkkkkkktwwwwwxuurrrrrtyyyyyokkkkzaarnnnnaxxxxxkrrqaaeccueebggydddddfoofllllvttttdjjjjsddddglllllxllllxffffjeeeevllllqrrrrvuuuikkkkzllwyyyyqttbaaaavyyyyynnnnbccuvvvzbbbzhhvdddrrfoosxxxxwoooooeggggzeeenttttteeeeeeeqqqqqbgggxnnnnqwwwwwyeetppppdeebaaaaardddddbhhhhskkeuuwxxhssssshdddvwwwlqqxaaadbbbbbkgggtssunnnnxcccvpppppsmmmmtiiiiithhiwwrqqqqzxxxxulllllvttpwwwwlzzfwwwwwlcchrrrmtttgwwwrwwwazzqaamwwwdkkksttqhhhhhcbbbbbtpppzssgeeeenrrrrrdyyyyyjeetxxxxvzzzzzvdddcttttgqqqqojjjjjolluzzzzzvcchwwwwwhrrkqqahhrgggmfffffidddddxccjoooonuuuuwjjjjjyvvvqeeeqooooxtttixxpoooojccccccmmfssssywwwwdffinnnnnsccyiipeeeecffffijjjjjfttttlwwwwwsrrroxxxwhhhhvffptttttcssaeedfffawwwweyygkkkkkucchfffqcccccstttttofffffgrrrxtttttqgggwmmmnpptiiiixvvvvvmqqkggtttttshhhhvkkkkfuupjjhuuugfffjvvbyynooooowyyynccwtteddddcmmwsszffffpccweeaccmooohhhhhhijjjjjwwwmpppppfkkkkkoaaftttteiiiiiybbbbbcsssssnzzuuuysssssvlllbpppppezzniiqjjjjjnyyrbbassdsssgjjjxhhhhdvvvvvqzzmrrjffffftqqkiiiiettttvwwwwrkkevvgbbbbbjttttyjjjncccchyyyyymjjjnmmmmmrddddewwwwyttttxvvvvvrhhhuyyyyyxzzzzqqqqqqzzzullllqzzngghaaefffffeccccchiiiepppppjyyyyoddgssssshttttvmmmmmebbgfffffuiiiiaqqqqhtttvkkkoeeeeevoooooviiiiidyysxxxojjjjjhvvvsbbbekkkabbqfffffdooyqqqqqrzzqxxxxorrrrrxzzzzznddddtjjjjeeecdddxuuummmvlllllzkkkkvhhhwwwwyiiiipsssaaaurrrrvwwwwwbttttvccuwwhkkkuqqruuuuzzzqyyyyymsssssgzzzzzsgggggmffriiiriiitnnnnnznnigggyssssnddddunnmjjjjcvvvnqqqqslldzzzzzsssssstjjjjzbbbajjjmuuuuucddddqqcpppppcxxczzxkkkkfnnnesssjllllljccccutttxkkkkuddmdddddjhhsaaaaagvvvouuuuugeeecjjjcmmyjjjjjrnnnntuuuuuhnnnnjzzzzlxxxxqiiiiiyaaaaazwwwwwueeeeijjjjjzyymiiiigzzgwwdzzbppvbbbbygguddddfqqfuuuuapppppnvvvvvrwwwwwshhhewwwlfffqlllztttttruuuuqkkwbbbbbpcccccwzzzazzztdddddbjjjnppmaaaazootmmmmmgxxxxxgbbbkeehkkkgmmmyrrrjnnnlootssrzzzwssssszhhhzzygggowwwwwpxxxxxcjjjjjisssspoooifffecccyyyyhaaqfffmmmfcccccohhhhhajjittuzzzzxxxxrqqqwooooaxxxxxkbbbbcnnruuuuukeeeexwwwsgggggidddddibbbbbtddcwwwwlddddxbbbbqxxxxxbrrrrrpeeeejhhqttttjppezzzhnnennnnninndgggqwwwwbmmmmmkmmmakkgjjjfkkkykkkkkbmmmmxbbbbrnnnnnebbbkeeeekmmmmokkkkbzzzzbfffrddddtaalkkkywwxqqtggghkkkkkqoodllllywwwwnllllpmmpddffffffeddqgggggaggggpzzzzkvvvvvwqqqqjnnnivvvbwwwsfffftmmmmmfrrrrrltttttjooooiiiiivsssbvvvvvxaaaaatnnnnvcccwxxxxnqqqueeeedaaaaaakkkkqlllliqqyddccccidddddkoooodiibrrrrrlwwwhyyyysddddaiiiidgggzttttieegrrrrrgaaaaaygggvyyykeeeedllllmyyyyyjjjjdrrdlllllgppppldddddtbbbbbiyyyyyrtttoccxgggmttvvvvsqqqqbqqqqqjhhhzuuuokkkkmzzznxxxxxxqqqtttvsszppppfqqqqqssssssezzzzkmmmmmgnnnnndiiiiigllllltxxxzqqqnddddrggzddannnnemmmmmtvvvvdnnnkyyyyyhggggvbbbfkkkkkhkkkknkkwhhgttttwccccuvvuiiiigyyyydpppajjjpiigccjjjjjjfmmmmhffdgggggkmmmgssoccaiiztttttquuybbbbbkmmmmkiiiywwwgwwwwluuujddekkkkkfnnnufffffqhhhspppppjbbbbrmmmyjjjkyywssiddepppppsooobiiiioqqqqqtqqswwwwlxxxgrrrioooooqjjpvvrzzzvwwwknnnnfssvxxxxxzkkkwvvvvqeeeutttttajjjjjocccccdcccctooooomggummodddcwwwwpnnnnjssssszcclhhetttejjjjnpptaazjjjkqqqqrnnwdddddhkkkknuuuuggggqooolmmmmmhyyyyyknnnnnpxxxxxzaaviiitooooojttxcccwrrmaaaurrrrtkkkkxhhhhyccccceyyyuwwhuuudvvvvvshhhhhayyyyksssssmvvvviwwwjccctzzzzzyiignnwjjjjjkrrrrrpjjeyyyyydqqexxxxxbyyyyoiiiiieddoyyyjvvvvvqwwwwwccvffmsssslaaaaopppoeewvvvvvnjjeeeeiwwwwwdssssonnnnjeeeevnnnnhwwwwuuheeeefqqtyyyyfssssseaaaaapeeeeefppppxvvnaaaaapiiepppekkkkktooooilllussssmqqqqqeggbbbbbitttturrrvyyywxxxckkkyrrrrmmmmiiiiaccccckkkkkddddduccfnnnnnnbbbbbfggiggggyffoooolyyilllazzwfffrmmwooolgggggkhhhhhdaaiffdggbxxwjjjjjuooocqqqmjjjjuzzzzgxxtqqqtkkkkkjzzukkktwwwwdaaaaadddddknnkooluuuuuxoooznnnnsggghrrrajjjrkkkskkkkktggggayyyyycwwwwxiiurrphhhhdeezyyyypaabddmwwwwnyyyyvuuyjjjjjqpppppojjjjsyyabbaxxriiidllllloyysxxxxpmmmbtttvjjjjioooraaucccwnnnnnziiiiibffffpoooimmmgkkkmqqtbbbbbliiiigfffgdddbwwwwwkkktrrrrvccctssssszooooogvvvvpuuypppppmcccccxyyyuccccyhhhhsxxxczzzzfpppsuuuufyyvuuvffullllqcchwwwwwoyyydkkkkuxxxffffiaaaaakppsbbjxxxlffffzwwwhhhhdggggaqqvyyyyieeeevmmmajjjqqqqqchhhoowzzzzzsffffzgggzeeeeqnndbbbbbhwwwqjjjjjpkknwwwllldzzkkkkfyyyhbbqcceggggghaaaidddddbttyjjjjstttttxrraaaaawqqqyaaaacssssszmmmmljjolllllpkkkkyrrrgmmmmfrrrummmmliiiiibmmmtnnnnatttttlrrrrqssweeeeerfffffnppppbiizqqqqytttttdxxxxoqqicccmwwwqkkkimmmcjjjhbbbbbcrrrkgggggittmwwwwwtttttqooopiilxxqllllhkkkkxmmmqzzswwwwwxjjjxqqqvmmmyqqqqqtxxxxclllllbnnnnnsooooullllthheuuuoqqgeeuzzzzmllljuuuuuzmmmyxxxqjjhvvvvvysssssmbbbbbyiitzzzzcqqqqloooooxjjjzttwcccrmmoaadggettttthiiiiidzzzbeeeeekhhjzzzzzullpdddobbvwwwwfssgccdccmpplhhhhhduuugttttbaaaaaicccgdddnkkkettttqvvvlrrroooooannnxffffvuuuossszqqqqqyppppggtiiiiiadddddtggggqhhhzpppppuxxxurrvuuuuukmmmigggayyyybbbbnjjjjzeeeeeyvvmmmmmxccxmmhxxxxnyyxvvvvvtgggjzzzzsaaaaaobbbbjooqkkkkoaaaaamttdkkkmcccccajjjjkkkkkfwwwwxvvbffillldkkkouuuugxxuddsvvvozzzzzovvpbbcbbtxxxxxjbbvtttttwaaagggggxqqijjjhzzzgtttttjjjjilltkkkkkvdddxjjjjqzzzzzjjjtiiiigpppewwwwuvvvvkqqooookeeedpppdeeeefuuwccccccvvabbbbnhhguuaiiiwiiidiiulllyuuuulooowwwwwheeehjjjjjtffffkdddddivvysssneeepyypjjjzooooodzzceetcccccppqeeenlllllzvvvvnddoyyesssskmmmmmecccciaaaaakkkaeeeepjjjjjtwwwwwcddesssssannnfhhdcccccbvvvvvthhhhhzxxxeiiljjjlnnnnmdddddchhhjjjjjkbbbbbsccccbzzwiiiqvvvvfwwwwweeeuvvtoowqqyiiiyuuuuuuaaaaazffffsrrjpppppsppemmmmmnffffntttidddddtaaaazooooyaaauffffmggggiddddgbbbejjybbbxlllnuuuuuqaaaapoouwwwmddtoowooooghhmjjwooavvvvvwbbaaaaaafoonxxxxxgnnniffpbblhhqtttjyyyywddqxxerrrrrmaauyyyynuuuuunwwnyyyytcccccbeeeesyyyncccccfpppppiooooobbbbbuppfcccccgxxxdrrrrywwwwwsqqqqqkwwwqccxpppdrrrrijjjjayyyjrrkaaaaiwwwwrrrrqhhhhduuuuteeekeeeerjjsppppmdddtwwwwwkhhhhhspppgfffffyvvvvaiiiiinllllmggghbbbbjfffffswwwwrjjdjjirrrrrnaaaaaehhhhhucccccgdddufffffxeeeyssirrrrrmeeeprrrixxxoxxxxvpppuuuokklrrvmmrppieeeeexgggggruuuuweeeedyyyyyxxxxxmxxkppprttttnbbbuwwwrkkhhhfoooojqqqqcpppoiiheeeedoooodmmmmzwwwwwbllgwwwwwfppppavvvvvhwwwxeeeeclllmoooooinnnblllossssfpppppwssssgvvvkcccceeeevyyyyzeeeeebmmtnnehhhhreeeeeqjjjqjjjjjdyyyijjpuuuuuypppppwhhtrrrrillllgrrrpyyyxllkxxxxdiiiipyyvooohjjjtpppppsaaaaahbbbeiiwffffflvvvvvsppppujjmqqqqoqqqqqqaaaazbbbbmrrroooooreeem'))
print(doubles('rrrmooomqqqqj'))