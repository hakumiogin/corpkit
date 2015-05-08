
# stopwords from spindle
stopwords = ["yeah", "monday","tuesday","wednesday","thursday","friday",
             "saturday","sunday","a","able","about","above","abst","accordance",
             "according","accordingly","across","act","actually","added","adj",
             "adopted","affected","affecting","affects","after","afterwards",
             "again","against","ah","all","almost","alone","along","already",
             "also","although","always","am","among","amongst","an","and",
             "announce","another","any","anybody","anyhow","anymore","anyone",
             "anything","anyway","anyways","anywhere","apparently","approximately",
             "are","aren","arent","arise","around","as","aside","ask","asking","at",
             "auth","available","away","awfully","b","back","be","became","because",
             "become","becomes","becoming","been","before","beforehand","begin",
             "beginning","beginnings","begins","behind","being","believe","below",
             "beside","besides","between","beyond","biol","both","brief","briefly",
             "but","by","c","ca","came","can","cannot","cant","cause","causes",
             "certain","certainly","co","com","come","comes","contain","containing",
             "contains","could","couldnt","d","date","did","didnt","different","do",
             "does","doesnt","doing","done","dont","down","downwards","due","during",
             "e","each","ed","edu","effect","eg","eight","eighty","either","else",
             "elsewhere","end","ending","enough","especially","et","et-al","etc","even",
             "ever","every","everybody","everyone","everything","everywhere","ex",
             "except","f","far","few","ff","fifth","first","five","fix","followed",
             "following","follows","for","former","formerly","forth","found","four",
             "from","further","furthermore","going","g","gave","get","gets","getting",
             "give","given","gives","giving","go","goes","gone","got","gotten","h",
             "had","happens","hardly","has","hasnt","have","havent","having","he",
             "hed","hence","her","here","hereafter","hereby","herein","heres",
             "hereupon","hers","herself","hes","hi","hid","him","himself","his",
             "hither","home","how","howbeit","however","hundred","i","id","ie",
             "if","ill","im","immediate","immediately","importance","important",
             "in","inc","indeed","index","information","instead","into","invention",
             "inward","is","isnt","it","itd","itll","its","itself","ive","j","just",
             "k","keep","keeps","kept","keys","kg","km","know","known","knows",
             "l","largely","last","lately","later","latter","latterly","least","less",
             "lest","let","lets","like","liked","likely","line","little","ll","look",
             "looking","looks","ltd","m","made","mainly","make","makes","many","may",
             "maybe","me","mean","means","meantime","meanwhile","merely","mg","might",
             "million","miss","ml","more","moreover","most","mostly","mr","mrs","much",
             "mug","must","my","myself","n","na","name","namely","nay","nd","near",
             "nearly","necessarily","necessary","need","needs","neither","never",
             "nevertheless","new","next","nine","ninety","no","nobody","non","none",
             "nonetheless","noone","nor","normally","nos","not","noted","nothing",
             "now","nowhere","o","obtain","obtained","obviously","of","off","often",
             "oh","ok","okay","old","omitted","on","once","one","ones","only","onto",
             "or","ord","other","others","otherwise","ought","our","ours","ourselves",
             "out","outside","over","overall","owing","own","p","page","pages","part",
             "particular","particularly","past","per","perhaps","placed","please",
             "plus","poorly","possible","possibly","potentially","pp","predominantly",
             "present","previously","primarily","probably","promptly","proud","provides",
             "put","q","que","quickly","quite","qv","r","ran","rather","rd","re",
             "readily","really","recent","recently","ref","refs","regarding","regardless",
             "regards","related","relatively","research","respectively","resulted",
             "resulting","results","right","run","s","said","same","saw","say","saying",
             "says","sec","section","see","seeing","seem","seemed","seeming","seems",
             "seen","self","selves","sent","seven","several","shall","she","shed","shell",
             "shes","should","shouldnt","show","showed","shown","showns","shows",
             "significant","significantly","similar","similarly","since","six",
             "slightly","so","some","somebody","somehow","someone","somethan","something",
             "sometime","sometimes","somewhat","somewhere","soon","sorry","specifically",
             "specified","specify","specifying","state","states","still","stop",
             "strongly","sub","substantially","successfully","such","sufficiently",
             "suggest","sup","sure","t","take","taken","taking","tell","tends","th",
             "than","thank","thanks","thanx","that","thatll","thats","thatve","the",
             "their","theirs","them","themselves","then","thence","there","thereafter",
             "thereby","thered","therefore","therein","therell","thereof","therere",
             "theres","thereto","thereupon","thereve","these","they","theyd","theyll",
             "theyre","theyve","think","this","those","thou","though","thoughh","thousand",
             "throug","through","throughout","thru","thus","til","tip","to","together",
             "too","took","toward","towards","tried","tries","truly","try","trying",
             "ts","twice","two","u","un","under","unfortunately","unless","unlike",
             "unlikely","until","unto","up","upon","ups","us","use","used","useful",
             "usefully","usefulness","uses","using","usually","v","value","various","ve",
             "very","via","viz","vol","vols","vs","w","want","wants","was","wasnt","way",
             "we","wed","welcome","well","went","were","werent","weve","what","whatever",
             "whatll","whats","when","whence","whenever","where","whereafter","whereas",
             "whereby","wherein","wheres","whereupon","wherever","whether","which",
             "while","whim","whither","who","whod","whoever","whole","wholl","whom",
             "whomever","whos","whose","why","widely","willing","wish","with","within",
             "without","wont","words","world","would","wouldnt","www","x","y","yes","yet",
             "you","youd","youll","your","youre","yours","yourself","yourselves","youve",
             "z","zero", "isn", "doesn","didn", "couldn", "mustn","shoudn","wasn","woudn",
             "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", 
             "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", 
             "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", 
             "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", 
             "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", 
             "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", 
             "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", 
             "about", "against", "between", "into", "through", "during", "before", "after", 
             "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", 
             "over", "under", "again", "further", "then", "once", "here", "there", "when", 
             "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", 
             "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", 
             "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", 
             "now", "gonna"]

# add nltk, justext and minilist here ...

justtext_stopwords = ["the","of","and","in","to","a","was","is","The","for","as","on","with","by","that","from","at","his","an","he","In","are","were","which","be","has","He","it","or","also","had","first","It","their","not","but","have","who","its","one","this","been","her","two","they","other","into","after","all","when","more","This","only","would","A","she","New","most","can","over","during","where","new","used","such","up","between","many","made","some","than","out","United","known","about","time","then","became","under","The","being","part","there","him","years","three","through","On","including","later","will","American","both","After","until","before","She","well","no","against","while","called","second","As","several","University","number","name","these","played","early","may","They","World","His","located","National","same","them","released","There","de","area","use","work","any","school","since","team","age","so","John","won","people","began","each","year","population","now","family","film","found","city","British","four","album","could","very","However","South","named","At","around","took","former","because","series","For","States","did","within","state","end","based","May","I","local","held","September","still","often","those","member","small","town","along","back","School","large","January","June","group","served","March","high","own","During","North","July","October","if","like","following","built","August","April","music","born","village","game","due","last","place","home","State","left","major","set","include","U.S","much","December","November","received","When","York","main","War","public","band","born","season","published","even","different","original","members","station","single","government","another","near","what","died","moved","become","just","February","company","included","song","came","led","late","form","national","make","went","These","off","show","French","five","system","few","various","given","best","English","City","long","third","among","every","West","German","using","do","said","started","currently","having","down","next","order","One","final","take","species","established","created","life","play","line","building","History","political","without","support","written","district","per","produced","High","popular","League","service","football","considered","St","way","returned","International","book","again","although","important","living","role","River","students","married","son","top","worked","San","continued","however","founded","joined","appeared","total","power","By","record","College","side","William","title","death","County","years","career","never","From","north","club","County","military","version","European","According","old","While","six","day","average","television","similar","world","general","million","With","Some","water","formed","international","usually","current","though","south","General","time","community","East","House","land","Although","George","making","player","playing","President","development","James","developed","common","should","great","century","does","further","run","working","largest","recorded","All","lost","must","elected","history","seen","live","opened","short","taken","once","professional","production","point","head","children","throughout","games","period","himself","originally","term","control","available","less","King","Its","modern","position","eventually","across","Royal","works","site","young","wrote","income","house","David","Other","Since","how","able","full","war","Australian","Air","London","Army","includes","law","designed","sold","featured","appointed","business","An","get","either","Japanese","program","US","Canadian","father","lead","approximately","performed","leading","radio","upon","remained","famous","Indian","we","Robert","First","help","west","gave","announced","men","result","times","field","you","right","east","almost","country","story","Church","followed","good","days","signed","features","together","described","research","sent","open","special","close","see","To","character","social","miles","rather","life","Council","Western","the","party","official","years","church"]