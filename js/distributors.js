/* Meet Our Distributors — client logic and data preserved; see notes marked SITE. */
document.addEventListener("DOMContentLoaded", function () {
  var TOTAL_SEATS_PER_CONSTITUENCY = 5;

  var registrationPageUrl = "https://appsphereb2b.com/distributor-registration/"; /* SITE: was relative "/distributor-registration/"; absolute so it resolves outside WordPress */
  var contactPageUrl = "contact.html"; /* SITE: local contact page (was relative "/contact/") */

  var stateNetwork = {
    "Kerala": {
        "Thiruvananthapuram": [
            "Varkala",
            "Attingal",
            "Chirayinkeezhu",
            "Nedumangad",
            "Vamanapuram",
            "Kazhakkoottam",
            "Vattiyoorkavu",
            "Thiruvananthapuram",
            "Nemom",
            "Aruvikkara",
            "Parassala",
            "Kattakkada",
            "Kovalam",
            "Neyyattinkara"
        ],
        "Kollam": [
            "Karunagappally",
            "Chavara",
            "Kunnathur",
            "Kottarakkara",
            "Pathanapuram",
            "Punalur",
            "Chadayamangalam",
            "Kundara",
            "Kollam",
            "Eravipuram",
            "Chathannoor"
        ],
        "Pathanamthitta": [
            "Thiruvalla",
            "Ranni",
            "Aranmula",
            "Konni",
            "Adoor"
        ],
        "Alappuzha": [
            "Aroor",
            "Cherthala",
            "Alappuzha",
            "Ambalappuzha",
            "Kuttanad",
            "Haripad",
            "Kayamkulam",
            "Mavelikkara",
            "Chengannur"
        ],
        "Kottayam": [
            "Pala",
            "Kaduthuruthy",
            "Vaikom",
            "Ettumanoor",
            "Kottayam",
            "Puthuppally",
            "Changanassery",
            "Kanjirappally",
            "Poonjar"
        ],
        "Idukki": [
            "Devikulam",
            "Udumbanchola",
            "Thodupuzha",
            "Idukki",
            "Peerumade"
        ],
        "Ernakulam": [
            "Perumbavoor",
            "Angamaly",
            "Aluva",
            "Kalamassery",
            "Paravur",
            "Vypin",
            "Kochi",
            "Thripunithura",
            "Ernakulam",
            "Thrikkakara",
            "Kunnathunad",
            "Piravom",
            "Muvattupuzha",
            "Kothamangalam"
        ],
        "Thrissur": [
            "Chelakkara",
            "Kunnamkulam",
            "Guruvayur",
            "Manalur",
            "Wadakkanchery",
            "Ollur",
            "Thrissur",
            "Nattika",
            "Kaipamangalam",
            "Irinjalakuda",
            "Puthukkad",
            "Chalakudy",
            "Kodungallur"
        ],
        "Palakkad": [
            "Thrithala",
            "Pattambi",
            "Shornur",
            "Ottapalam",
            "Kongad",
            "Mannarkkad",
            "Malampuzha",
            "Palakkad",
            "Tarur",
            "Chittur",
            "Nemmara",
            "Alathur"
        ],
        "Malappuram": [
            "Kondotty",
            "Eranad",
            "Nilambur",
            "Wandoor",
            "Manjeri",
            "Perinthalmanna",
            "Mankada",
            "Malappuram",
            "Vengara",
            "Vallikkunnu",
            "Tirurangadi",
            "Tanur",
            "Tirur",
            "Kottakkal",
            "Thavanur",
            "Ponnani"
        ],
        "Kozhikode": [
            "Vadakara",
            "Kuttiady",
            "Nadapuram",
            "Koyilandy",
            "Perambra",
            "Balussery",
            "Elathur",
            "Kozhikode North",
            "Kozhikode South",
            "Beypore",
            "Kunnamangalam",
            "Koduvally",
            "Thiruvambady"
        ],
        "Wayanad": [
            "Mananthavady",
            "Sulthan Bathery",
            "Kalpetta"
        ],
        "Kannur": [
            "Payyannur",
            "Kalliasseri",
            "Taliparamba",
            "Irikkur",
            "Azhikode",
            "Kannur",
            "Dharmadom",
            "Thalassery",
            "Kuthuparamba",
            "Mattannur",
            "Peravoor"
        ],
        "Kasaragod": [
            "Manjeshwar",
            "Kasaragod",
            "Udma",
            "Kanhangad",
            "Trikaripur"
        ]
    },
    "Tamil Nadu": {
        "Thiruvallur": [
            "Gummidipoondi",
            "Ponneri",
            "Tiruttani",
            "Thiruvallur",
            "Poonamallee",
            "Avadi",
            "Maduravoyal",
            "Ambattur",
            "Madavaram",
            "Thiruvottiyur"
        ],
        "Chennai": [
            "Dr. Radhakrishnan Nagar",
            "Perambur",
            "Kolathur",
            "Villivakkam",
            "Thiru-Vi-Ka-Nagar",
            "Egmore",
            "Royapuram",
            "Harbour",
            "Chepauk-Thiruvallikeni",
            "Thousand Lights",
            "Anna Nagar",
            "Virugampakkam",
            "Saidapet",
            "Thiyagarayanagar",
            "Mylapore",
            "Velachery"
        ],
        "Chengalpattu": [
            "Shozhinganallur",
            "Alandur",
            "Pallavaram",
            "Tambaram",
            "Chengalpattu",
            "Thiruporur",
            "Cheyyur",
            "Madurantakam"
        ],
        "Kancheepuram": [
            "Sriperumbudur",
            "Uthiramerur",
            "Kancheepuram"
        ],
        "Ranipet": [
            "Arakkonam",
            "Sholinghur",
            "Ranipet",
            "Arcot"
        ],
        "Vellore": [
            "Katpadi",
            "Vellore",
            "Anaikattu",
            "Kilvaithinankuppam",
            "Gudiyattam"
        ],
        "Tirupattur": [
            "Vaniyambadi",
            "Ambur",
            "Jolarpet",
            "Tirupattur"
        ],
        "Krishnagiri": [
            "Uthangarai",
            "Bargur",
            "Krishnagiri",
            "Veppanahalli",
            "Hosur",
            "Thalli"
        ],
        "Dharmapuri": [
            "Palacode",
            "Pennagaram",
            "Dharmapuri",
            "Pappireddipatti",
            "Harur"
        ],
        "Tiruvannamalai": [
            "Chengam",
            "Tiruvannamalai",
            "Kilpennathur",
            "Kalasapakkam",
            "Polur",
            "Arani",
            "Cheyyar",
            "Vandavasi"
        ],
        "Villupuram": [
            "Gingee",
            "Mailam",
            "Tindivanam",
            "Vanur",
            "Villupuram",
            "Vikravandi"
        ],
        "Kallakurichi": [
            "Tirukkoyilur",
            "Ulundurpettai",
            "Rishivandiyam",
            "Sankarapuram",
            "Kallakurichi"
        ],
        "Salem": [
            "Gangavalli",
            "Attur",
            "Yercaud",
            "Omalur",
            "Mettur",
            "Edappadi",
            "Sankari",
            "Salem West",
            "Salem North",
            "Salem South",
            "Veerapandi"
        ],
        "Namakkal": [
            "Rasipuram",
            "Senthamangalam",
            "Namakkal",
            "Paramathi-Velur",
            "Tiruchengodu",
            "Kumarapalayam"
        ],
        "Erode": [
            "Erode East",
            "Erode West",
            "Modakkurichi",
            "Perundurai",
            "Bhavani",
            "Anthiyur",
            "Gobichettipalayam"
        ],
        "Tiruppur": [
            "Dharapuram",
            "Kangayam",
            "Avanashi",
            "Tiruppur North",
            "Tiruppur South",
            "Palladam",
            "Udumalaipettai",
            "Madathukulam"
        ],
        "The Nilgiris": [
            "Bhavanisagar",
            "Udhagamandalam",
            "Gudalur",
            "Coonoor"
        ],
        "Coimbatore": [
            "Mettuppalayam",
            "Sulur",
            "Kavundampalayam",
            "Coimbatore North",
            "Thondamuthur",
            "Coimbatore South",
            "Singanallur",
            "Kinathukadavu",
            "Pollachi",
            "Valparai"
        ],
        "Dindigul": [
            "Palani",
            "Oddanchatram",
            "Athoor",
            "Nilakkottai",
            "Natham",
            "Dindigul",
            "Vedasandur"
        ],
        "Karur": [
            "Aravakurichi",
            "Karur",
            "Krishnarayapuram",
            "Kulithalai"
        ],
        "Tiruchirappalli": [
            "Manapparai",
            "Srirangam",
            "Tiruchirappalli West",
            "Tiruchirappalli East",
            "Thiruverumbur",
            "Lalgudi",
            "Manachanallur",
            "Musiri",
            "Thuraiyur"
        ],
        "Perambalur": [
            "Perambalur",
            "Kunnam"
        ],
        "Ariyalur": [
            "Ariyalur",
            "Jayankondam"
        ],
        "Cuddalore": [
            "Tittakudi",
            "Vriddhachalam",
            "Neyveli",
            "Panruti",
            "Cuddalore",
            "Kurinjipadi",
            "Bhuvanagiri",
            "Chidambaram",
            "Kattumannarkoil"
        ],
        "Mayiladuthurai": [
            "Sirkazhi",
            "Mayiladuthurai",
            "Poompuhar"
        ],
        "Nagapattinam": [
            "Nagapattinam",
            "Kilvelur",
            "Vedaranyam"
        ],
        "Thiruvarur": [
            "Thiruthuraipoondi",
            "Mannargudi",
            "Thiruvarur",
            "Nannilam"
        ],
        "Thanjavur": [
            "Thiruvidaimarudur",
            "Kumbakonam",
            "Papanasam",
            "Thiruvaiyaru",
            "Thanjavur",
            "Orathanadu",
            "Pattukkottai",
            "Peravurani"
        ],
        "Pudukkottai": [
            "Gandarvakkottai",
            "Viralimalai",
            "Pudukkottai",
            "Thirumayam",
            "Alangudi",
            "Aranthangi"
        ],
        "Sivaganga": [
            "Karaikudi",
            "Tiruppattur",
            "Sivaganga",
            "Manamadurai"
        ],
        "Madurai": [
            "Melur",
            "Madurai East",
            "Sholavandan",
            "Madurai North",
            "Madurai South",
            "Madurai Central",
            "Madurai West",
            "Thiruparankundram",
            "Thirumangalam",
            "Usilampatti"
        ],
        "Theni": [
            "Andipatti",
            "Periyakulam",
            "Bodinayakanur",
            "Cumbum"
        ],
        "Virudhunagar": [
            "Rajapalayam",
            "Srivilliputhur",
            "Sattur",
            "Sivakasi",
            "Virudhunagar",
            "Aruppukkottai",
            "Tiruchuli"
        ],
        "Ramanathapuram": [
            "Paramakudi",
            "Tiruvadanai",
            "Ramanathapuram",
            "Mudhukulathur"
        ],
        "Thoothukudi": [
            "Vilathikulam",
            "Thoothukkudi",
            "Tiruchendur",
            "Srivaikuntam",
            "Ottapidaram",
            "Kovilpatti"
        ],
        "Tenkasi": [
            "Sankarankovil",
            "Vasudevanallur",
            "Kadayanallur",
            "Tenkasi",
            "Alangulam"
        ],
        "Tirunelveli": [
            "Tirunelveli",
            "Ambasamudram",
            "Palayamkottai",
            "Nanguneri",
            "Radhapuram"
        ],
        "Kanniyakumari": [
            "Kanniyakumari",
            "Nagercoil",
            "Colachal",
            "Padmanabhapuram",
            "Vilavancode",
            "Killiyoor"
        ]
    },
    "Karnataka": {
        "Belagavi": [
            "Nippani",
            "Chikkodi-Sadalga",
            "Athani",
            "Kagwad",
            "Kudachi",
            "Raybag",
            "Hukkeri",
            "Arabhavi",
            "Gokak",
            "Yemkanmardi",
            "Belgaum Uttar",
            "Belgaum Dakshin",
            "Belgaum Rural",
            "Khanapur",
            "Kittur",
            "Bailhongal",
            "Saundatti Yellamma",
            "Ramdurg"
        ],
        "Bagalkote": [
            "Mudhol",
            "Terdal",
            "Jamkhandi",
            "Bilgi",
            "Badami",
            "Bagalkot",
            "Hungund"
        ],
        "Vijayapura": [
            "Muddebihal",
            "Devar Hippargi",
            "Basavana Bagevadi",
            "Babaleshwar",
            "Bijapur City",
            "Nagthan",
            "Indi",
            "Sindgi"
        ],
        "Yadgir": [
            "Shorapur",
            "Shahapur",
            "Yadgir",
            "Gurmitkal"
        ],
        "Kalaburagi": [
            "Afzalpur",
            "Jevargi",
            "Chittapur",
            "Sedam",
            "Chincholi",
            "Gulbarga Rural",
            "Gulbarga Dakshin",
            "Gulbarga Uttar",
            "Aland"
        ],
        "Bidar": [
            "Basavakalyan",
            "Humnabad",
            "Bidar South",
            "Bidar",
            "Bhalki",
            "Aurad"
        ],
        "Raichur": [
            "Raichur Rural",
            "Raichur",
            "Manvi",
            "Devadurga",
            "Lingsugur",
            "Sindhanur",
            "Maski"
        ],
        "Koppal": [
            "Kushtagi",
            "Kanakagiri",
            "Gangavathi",
            "Yelburga",
            "Koppal"
        ],
        "Gadag": [
            "Shirahatti",
            "Gadag",
            "Ron",
            "Nargund"
        ],
        "Dharwad": [
            "Navalgund",
            "Kundgol",
            "Dharwad",
            "Hubli-Dharwad-East",
            "Hubli-Dharwad-Central",
            "Hubli-Dharwad-West",
            "Kalaghatgi"
        ],
        "Uttara Kannada": [
            "Haliyal",
            "Karwar",
            "Kumta",
            "Bhatkal",
            "Sirsi",
            "Yellapur"
        ],
        "Haveri": [
            "Hangal",
            "Shiggaon",
            "Haveri",
            "Byadgi",
            "Hirekerur",
            "Ranebennur"
        ],
        "Vijayanagara": [
            "Hadagali",
            "Hagaribommanahalli",
            "Vijayanagara",
            "Kudligi",
            "Harapanahalli"
        ],
        "Ballari": [
            "Kampli",
            "Siraguppa",
            "Bellary",
            "Bellary City",
            "Sandur"
        ],
        "Chitradurga": [
            "Molakalmuru",
            "Challakere",
            "Chitradurga",
            "Hiriyur",
            "Hosadurga",
            "Holalkere"
        ],
        "Davanagere": [
            "Jagalur",
            "Harihar",
            "Davanagere North",
            "Davanagere South",
            "Mayakonda",
            "Channagiri",
            "Honnali"
        ],
        "Shivamogga": [
            "Shimoga Rural",
            "Bhadravathi",
            "Shimoga",
            "Tirthahalli",
            "Shikaripura",
            "Sorab",
            "Sagar"
        ],
        "Udupi": [
            "Baindur",
            "Kundapur",
            "Udupi",
            "Kaup",
            "Karkala"
        ],
        "Chikkamagaluru": [
            "Sringeri",
            "Mudigere",
            "Chickamagalur",
            "Tarikere",
            "Kadur"
        ],
        "Tumakuru": [
            "Chiknayakanhalli",
            "Tiptur",
            "Turuvekere",
            "Kunigal",
            "Tumkur City",
            "Tumkur Rural",
            "Koratagere",
            "Gubbi",
            "Sira",
            "Pavagada",
            "Madhugiri"
        ],
        "Chikkaballapura": [
            "Gauribidanur",
            "Bagepalli",
            "Chikkaballapur",
            "Sidlaghatta",
            "Chintamani"
        ],
        "Kolar": [
            "Srinivasapur",
            "Mulbagal",
            "Kolar Gold Field",
            "Bangarapet",
            "Kolar",
            "Malur"
        ],
        "Bengaluru Urban": [
            "Rajarajeshwarinagar",
            "K.R. Pura",
            "Shivajinagar",
            "Shantinagar",
            "Gandhinagar",
            "Rajajinagar",
            "Mahalakshmi Layout",
            "Malleshwaram",
            "Hebbal",
            "Pulakeshinagar",
            "Sarvagnanagar",
            "C.V. Raman Nagar",
            "Govindarajanagar",
            "Vijayanagar",
            "Chamrajpet",
            "Chickpet",
            "Basavanagudi",
            "Padmanabhanagar",
            "B.T.M. Layout",
            "Jayanagar",
            "Mahadevapura",
            "Bommanahalli",
            "Bangalore South",
            "Anekal"
        ],
        "Bengaluru Rural": [
            "Yelahanka",
            "Byatarayanapura",
            "Yeshwanthapura",
            "Dasarahalli",
            "Devanahalli",
            "Doddaballapur",
            "Nelamangala",
            "Hosakote"
        ],
        "Ramanagara": [
            "Magadi",
            "Ramanagaram",
            "Kanakapura",
            "Channapatna"
        ],
        "Mandya": [
            "Malavalli",
            "Maddur",
            "Melukote",
            "Mandya",
            "Srirangapatna",
            "Nagamangala",
            "Krishnarajpet"
        ],
        "Hassan": [
            "Shravanabelagola",
            "Arsikere",
            "Belur",
            "Hassan",
            "Holenarasipur",
            "Arkalgud",
            "Sakleshpur"
        ],
        "Dakshina Kannada": [
            "Belthangady",
            "Moodabidri",
            "Mangalore City North",
            "Mangalore City South",
            "Mangalore",
            "Bantwal",
            "Puttur",
            "Sullia"
        ],
        "Kodagu": [
            "Madikeri",
            "Virajpet"
        ],
        "Mysuru": [
            "Piriyapatna",
            "Krishnarajanagara",
            "Hunsur",
            "Heggadadevankote",
            "Nanjangud",
            "Chamundeshwari",
            "Krishnaraja",
            "Chamaraja",
            "Narasimharaja",
            "Varuna",
            "T. Narasipur"
        ],
        "Chamarajanagar": [
            "Hanur",
            "Kollegal",
            "Chamarajanagar",
            "Gundlupet"
        ]
    },
    "Andhra Pradesh": {
        "Srikakulam": [
            "Ichchapuram",
            "Palasa",
            "Tekkali",
            "Pathapatnam",
            "Srikakulam",
            "Amadalavalasa",
            "Etcherla",
            "Narasannapeta"
        ],
        "Vizianagaram": [
            "Rajam",
            "Bobbili",
            "Cheepurupalli",
            "Gajapathinagaram",
            "Nellimarla",
            "Vizianagaram",
            "Srungavarapukota"
        ],
        "Parvathipuram Manyam": [
            "Palakonda",
            "Kurupam",
            "Parvathipuram",
            "Salur"
        ],
        "Alluri Sitharama Raju": [
            "Araku Valley",
            "Paderu",
            "Rampachodavaram"
        ],
        "Visakhapatnam": [
            "Bhimili",
            "Visakhapatnam East",
            "Visakhapatnam South",
            "Visakhapatnam North",
            "Visakhapatnam West",
            "Gajuwaka"
        ],
        "Anakapalli": [
            "Chodavaram",
            "Madugula",
            "Anakapalle",
            "Pendurthi",
            "Elamanchili",
            "Payakaraopet",
            "Narsipatnam"
        ],
        "Kakinada": [
            "Tuni",
            "Prathipadu",
            "Pithapuram",
            "Kakinada Rural",
            "Peddapuram",
            "Kakinada City",
            "Jaggampeta"
        ],
        "Dr. B. R. Ambedkar Konaseema": [
            "Ramachandrapuram",
            "Mummidivaram",
            "Amalapuram",
            "Razole",
            "Gannavaram",
            "Kothapeta",
            "Mandapeta"
        ],
        "East Godavari": [
            "Anaparthy",
            "Rajanagaram",
            "Rajahmundry City",
            "Rajahmundry Rural",
            "Kovvur",
            "Nidadavole",
            "Gopalapuram"
        ],
        "West Godavari": [
            "Achanta",
            "Palacole",
            "Narasapuram",
            "Bhimavaram",
            "Undi",
            "Tanuku",
            "Tadepalligudem"
        ],
        "Eluru": [
            "Ungutur",
            "Denduluru",
            "Eluru",
            "Polavaram",
            "Chintalapudi",
            "Nuzvid",
            "Kaikalur"
        ],
        "Krishna": [
            "Gannavaram",
            "Gudivada",
            "Pedana",
            "Machilipatnam",
            "Avanigadda",
            "Pamarru",
            "Penamaluru"
        ],
        "NTR": [
            "Tiruvuru",
            "Vijayawada West",
            "Vijayawada Central",
            "Vijayawada East",
            "Mylavaram",
            "Nandigama",
            "Jaggayyapeta"
        ],
        "Guntur": [
            "Tadikonda",
            "Mangalagiri",
            "Ponnur",
            "Tenali",
            "Prathipadu",
            "Guntur West",
            "Guntur East"
        ],
        "Bapatla": [
            "Vemuru",
            "Repalle",
            "Bapatla",
            "Parchur",
            "Addanki",
            "Chirala"
        ],
        "Palnadu": [
            "Pedakurapadu",
            "Chilakaluripet",
            "Narasaraopet",
            "Sattenapalle",
            "Vinukonda",
            "Gurajala",
            "Macherla"
        ],
        "Prakasam": [
            "Yerragondapalem",
            "Darsi",
            "Santhanuthalapadu",
            "Ongole",
            "Kondapi",
            "Markapuram",
            "Giddalur",
            "Kanigiri"
        ],
        "Sri Potti Sriramulu Nellore": [
            "Kandukur",
            "Kavali",
            "Atmakur",
            "Kovur",
            "Nellore City",
            "Nellore Rural",
            "Sarvepalli",
            "Udayagiri"
        ],
        "Tirupati": [
            "Gudur",
            "Sullurpeta",
            "Venkatagiri",
            "Tirupati",
            "Srikalahasti",
            "Satyavedu"
        ],
        "YSR Kadapa": [
            "Badvel",
            "Kadapa",
            "Pulivendla",
            "Kamalapuram",
            "Jammalamadugu",
            "Proddatur",
            "Mydukur"
        ],
        "Annamayya": [
            "Rajampet",
            "Kodur",
            "Rayachoti",
            "Pileru",
            "Madanapalle",
            "Thamballapalle"
        ],
        "Kurnool": [
            "Kurnool",
            "Panyam",
            "Pattikonda",
            "Kodumur",
            "Yemmiganur",
            "Mantralayam",
            "Adoni",
            "Alur"
        ],
        "Nandyal": [
            "Allagadda",
            "Srisailam",
            "Nandikotkur",
            "Nandyal",
            "Banaganapalle",
            "Dhone"
        ],
        "Anantapuramu": [
            "Rayadurg",
            "Uravakonda",
            "Guntakal",
            "Tadpatri",
            "Singanamala",
            "Anantapur Urban",
            "Kalyandurg",
            "Raptadu"
        ],
        "Sri Sathya Sai": [
            "Madakasira",
            "Hindupur",
            "Penukonda",
            "Puttaparthi",
            "Dharmavaram",
            "Kadiri"
        ],
        "Chittoor": [
            "Thamballapalle",
            "Punganur",
            "Chandragiri",
            "Chittoor",
            "Puthalapattu",
            "Palamaner",
            "Kuppam",
            "Nagari"
        ]
    },
    "Telangana": {
        "Kumaram Bheem Asifabad": [
            "Sirpur",
            "Asifabad"
        ],
        "Mancherial": [
            "Chennur",
            "Bellampalli",
            "Mancherial"
        ],
        "Adilabad": [
            "Adilabad",
            "Boath"
        ],
        "Nirmal": [
            "Nirmal",
            "Mudhole",
            "Khanapur"
        ],
        "Nizamabad": [
            "Armur",
            "Bodhan",
            "Nizamabad Urban",
            "Nizamabad Rural",
            "Balkonda"
        ],
        "Kamareddy": [
            "Jukkal",
            "Yellareddy",
            "Kamareddy",
            "Banswada"
        ],
        "Jagtial": [
            "Koratla",
            "Jagtial",
            "Dharmapuri"
        ],
        "Peddapalli": [
            "Ramagundam",
            "Manthani",
            "Peddapalle"
        ],
        "Karimnagar": [
            "Karimnagar",
            "Choppadandi",
            "Manakondur",
            "Huzurabad"
        ],
        "Rajanna Sircilla": [
            "Vemulawada",
            "Sircilla"
        ],
        "Siddipet": [
            "Siddipet",
            "Husnabad",
            "Dubbak",
            "Gajwel"
        ],
        "Medak": [
            "Medak",
            "Narsapur"
        ],
        "Sangareddy": [
            "Sangareddy",
            "Patancheru",
            "Andole",
            "Narayankhed",
            "Zaheerabad"
        ],
        "Medchal-Malkajgiri": [
            "Medchal",
            "Malkajgiri",
            "Quthbullapur",
            "Kukatpally",
            "Uppal"
        ],
        "Hyderabad": [
            "Musheerabad",
            "Malakpet",
            "Amberpet",
            "Khairatabad",
            "Jubilee Hills",
            "Sanathnagar",
            "Nampally",
            "Karwan",
            "Goshamahal",
            "Charminar",
            "Chandrayangutta",
            "Yakutpura",
            "Bahadurpura",
            "Secunderabad",
            "Secunderabad Cantonment"
        ],
        "Rangareddy": [
            "Ibrahimpatnam",
            "L. B. Nagar",
            "Maheshwaram",
            "Rajendranagar",
            "Serilingampally",
            "Chevella",
            "Pargi"
        ],
        "Vikarabad": [
            "Vikarabad",
            "Tandur",
            "Kodangal"
        ],
        "Mahabubnagar": [
            "Mahabubnagar",
            "Jadcherla",
            "Devarkadra"
        ],
        "Narayanpet": [
            "Narayanpet",
            "Makthal"
        ],
        "Jogulamba Gadwal": [
            "Gadwal",
            "Alampur"
        ],
        "Wanaparthy": [
            "Wanaparthy"
        ],
        "Nagarkurnool": [
            "Nagarkurnool",
            "Achampet",
            "Kalwakurthy",
            "Shadnagar",
            "Kollapur"
        ],
        "Nalgonda": [
            "Devarakonda",
            "Nagarjuna Sagar",
            "Miryalaguda",
            "Nalgonda",
            "Munugode",
            "Nakrekal"
        ],
        "Suryapet": [
            "Suryapet",
            "Kodad",
            "Huzurnagar",
            "Thungathurthi"
        ],
        "Yadadri Bhuvanagiri": [
            "Alair",
            "Bhongir"
        ],
        "Jangaon": [
            "Jangaon",
            "Ghanpur Station",
            "Palakurthi"
        ],
        "Mahabubabad": [
            "Dornakal",
            "Mahabubabad"
        ],
        "Warangal": [
            "Warangal East",
            "Warangal West",
            "Narsampet"
        ],
        "Hanamkonda": [
            "Parkal",
            "Wardhannapet"
        ],
        "Jayashankar Bhupalpally": [
            "Bhupalpalle"
        ],
        "Mulugu": [
            "Mulug"
        ],
        "Bhadradri Kothagudem": [
            "Pinapaka",
            "Yellandu",
            "Bhadrachalam",
            "Kothagudem",
            "Aswaraopeta"
        ],
        "Khammam": [
            "Khammam",
            "Palair",
            "Madhira",
            "Wyra",
            "Sathupalli"
        ]
    },
    "Maharashtra": {
        "Nandurbar": [
            "Akkalkuwa",
            "Shahada",
            "Nandurbar",
            "Nawapur"
        ],
        "Dhule": [
            "Sakri",
            "Dhule Rural",
            "Dhule City",
            "Sindkheda",
            "Shirpur"
        ],
        "Jalgaon": [
            "Chopda",
            "Raver",
            "Bhusawal",
            "Jalgaon City",
            "Jalgaon Rural",
            "Amalner",
            "Erandol",
            "Chalisgaon",
            "Pachora",
            "Jamner",
            "Muktainagar"
        ],
        "Buldhana": [
            "Malkapur",
            "Buldhana",
            "Chikhli",
            "Sindkhed Raja",
            "Mehkar",
            "Khamgaon",
            "Jalgaon Jamod"
        ],
        "Akola": [
            "Akot",
            "Balapur",
            "Akola West",
            "Akola East",
            "Murtizapur"
        ],
        "Washim": [
            "Risod",
            "Washim",
            "Karanja"
        ],
        "Amravati": [
            "Dhamangaon Railway",
            "Badnera",
            "Amravati",
            "Teosa",
            "Daryapur",
            "Melghat",
            "Achalpur",
            "Morshi"
        ],
        "Wardha": [
            "Arvi",
            "Deoli",
            "Hinganghat",
            "Wardha"
        ],
        "Nagpur": [
            "Katol",
            "Savner",
            "Hingna",
            "Umred",
            "Nagpur South West",
            "Nagpur South",
            "Nagpur East",
            "Nagpur Central",
            "Nagpur West",
            "Nagpur North",
            "Kamthi",
            "Ramtek"
        ],
        "Bhandara": [
            "Tumsar",
            "Bhandara",
            "Sakoli"
        ],
        "Gondia": [
            "Arjuni Morgaon",
            "Tirora",
            "Gondia",
            "Amgaon"
        ],
        "Gadchiroli": [
            "Armori",
            "Gadchiroli",
            "Aheri"
        ],
        "Chandrapur": [
            "Rajura",
            "Chandrapur",
            "Ballarpur",
            "Bramhapuri",
            "Chimur",
            "Warora"
        ],
        "Yavatmal": [
            "Wani",
            "Ralegaon",
            "Yavatmal",
            "Digras",
            "Arni",
            "Pusad",
            "Umarkhed"
        ],
        "Nanded": [
            "Kinwat",
            "Hadgaon",
            "Bhokar",
            "Nanded North",
            "Nanded South",
            "Loha",
            "Naigaon",
            "Deglur",
            "Mukhed"
        ],
        "Hingoli": [
            "Basmath",
            "Kalamnuri",
            "Hingoli"
        ],
        "Parbhani": [
            "Jintur",
            "Parbhani",
            "Gangakhed",
            "Pathri"
        ],
        "Jalna": [
            "Partur",
            "Ghansawangi",
            "Jalna",
            "Badnapur",
            "Bhokardan"
        ],
        "Chhatrapati Sambhajinagar": [
            "Sillod",
            "Kannad",
            "Phulambri",
            "Aurangabad Central",
            "Aurangabad West",
            "Aurangabad East",
            "Paithan",
            "Gangapur",
            "Vaijapur"
        ],
        "Nashik": [
            "Nandgaon",
            "Malegaon Central",
            "Malegaon Outer",
            "Baglan",
            "Kalwan",
            "Chandwad",
            "Yevla",
            "Sinnar",
            "Niphad",
            "Dindori",
            "Nashik East",
            "Nashik Central",
            "Nashik West",
            "Deolali",
            "Igatpuri"
        ],
        "Palghar": [
            "Dahanu",
            "Vikramgad",
            "Palghar",
            "Boisar",
            "Nalasopara",
            "Vasai"
        ],
        "Thane": [
            "Bhiwandi Rural",
            "Shahapur",
            "Bhiwandi West",
            "Bhiwandi East",
            "Kalyan West",
            "Murbad",
            "Ambarnath",
            "Ulhasnagar",
            "Kalyan East",
            "Dombivli",
            "Kalyan Rural",
            "Mira Bhayandar",
            "Ovala-Majiwada",
            "Kopri-Pachpakhadi",
            "Thane",
            "Mumbra-Kalwa",
            "Airoli",
            "Belapur"
        ],
        "Mumbai Suburban": [
            "Borivali",
            "Dahisar",
            "Magathane",
            "Mulund",
            "Vikhroli",
            "Bhandup West",
            "Jogeshwari East",
            "Dindoshi",
            "Kandivali East",
            "Charkop",
            "Malad West",
            "Goregaon",
            "Versova",
            "Andheri West",
            "Andheri East",
            "Vile Parle",
            "Chandivali",
            "Ghatkopar West",
            "Ghatkopar East",
            "Mankhurd Shivaji Nagar",
            "Anushakti Nagar",
            "Chembur",
            "Kurla",
            "Kalina",
            "Vandre East",
            "Vandre West"
        ],
        "Mumbai City": [
            "Dharavi",
            "Sion Koliwada",
            "Wadala",
            "Mahim",
            "Worli",
            "Shivadi",
            "Byculla",
            "Malabar Hill",
            "Mumbadevi",
            "Colaba"
        ],
        "Raigad": [
            "Panvel",
            "Karjat",
            "Uran",
            "Pen",
            "Alibag",
            "Shrivardhan",
            "Mahad"
        ],
        "Pune": [
            "Junnar",
            "Ambegaon",
            "Khed Alandi",
            "Shirur",
            "Daund",
            "Indapur",
            "Baramati",
            "Purandar",
            "Bhor",
            "Maval",
            "Chinchwad",
            "Pimpri",
            "Bhosari",
            "Vadgaon Sheri",
            "Shivajinagar",
            "Kothrud",
            "Khadakwasala",
            "Parvati",
            "Hadapsar",
            "Pune Cantonment",
            "Kasba Peth"
        ],
        "Ahmednagar": [
            "Akole",
            "Sangamner",
            "Shirdi",
            "Kopargaon",
            "Shrirampur",
            "Nevasa",
            "Shevgaon",
            "Rahuri",
            "Parner",
            "Ahmednagar City",
            "Shrigonda",
            "Karjat Jamkhed"
        ],
        "Beed": [
            "Georai",
            "Majalgaon",
            "Beed",
            "Ashti",
            "Kaij",
            "Parli"
        ],
        "Latur": [
            "Latur Rural",
            "Latur City",
            "Ahmadpur",
            "Udgir",
            "Nilanga",
            "Ausa"
        ],
        "Dharashiv": [
            "Omerga",
            "Tuljapur",
            "Osmanabad",
            "Paranda"
        ],
        "Solapur": [
            "Karmala",
            "Madha",
            "Barshi",
            "Mohol",
            "Solapur City North",
            "Solapur City Central",
            "Akkalkot",
            "Solapur South",
            "Pandharpur",
            "Sangole",
            "Malshiras"
        ],
        "Satara": [
            "Phaltan",
            "Wai",
            "Koregaon",
            "Man",
            "Karad North",
            "Karad South",
            "Patan",
            "Satara"
        ],
        "Ratnagiri": [
            "Dapoli",
            "Guhagar",
            "Chiplun",
            "Ratnagiri",
            "Rajapur"
        ],
        "Sindhudurg": [
            "Kankavli",
            "Kudal",
            "Sawantwadi"
        ],
        "Kolhapur": [
            "Chandgad",
            "Radhanagari",
            "Kagal",
            "Kolhapur South",
            "Karvir",
            "Kolhapur North",
            "Shahuwadi",
            "Hatkanangle",
            "Ichalkaranji",
            "Shirol"
        ],
        "Sangli": [
            "Miraj",
            "Sangli",
            "Islampur",
            "Shirala",
            "Palus-Kadegaon",
            "Khanapur",
            "Tasgaon-Kavathe Mahankal",
            "Jat"
        ]
    }
};

  /*
    EDIT REAL DISTRIBUTORS HERE ONLY.

    Keep the constituency name exactly same as above.

    To add multiple distributors in the same constituency,
    add multiple objects inside that constituency array.

    Example:
    "Cherthala": [
      { distributor 1 },
      { distributor 2 }
    ]
  */

  /* SITE: the client file shipped a placeholder "Mr. Sample Distributor" (Cherthala) with a placeholder photo.
     It is NOT shown publicly. Add real, consented distributors here using the same shape:
     "Cherthala": [ { name, tradeName, mobileDisplay, mobileLink, gstDisplay, addressDisplay, photo } ] */
  var distributorData = {};

  var stateSelect = document.getElementById("spState");
  var districtSelect = document.getElementById("spDistrict");
  var summarySection = document.getElementById("spDistrictSummary");
  var outputSection = document.getElementById("spConstituencyOutput");

  if (!stateSelect || !districtSelect || !summarySection || !outputSection) {
    return;
  }

  stateSelect.addEventListener("change", function () {
    districtSelect.innerHTML = '<option value="">Select District</option>';
    outputSection.innerHTML = "";
    summarySection.style.display = "none";

    if (stateSelect.value && stateNetwork[stateSelect.value]) {
      Object.keys(stateNetwork[stateSelect.value]).forEach(function (district) {
        var option = document.createElement("option");
        option.value = district;
        option.textContent = district;
        districtSelect.appendChild(option);
      });

      districtSelect.disabled = false;
    } else {
      districtSelect.disabled = true;
    }
  });

  districtSelect.addEventListener("change", function () {
    var selectedDistrict = districtSelect.value;

    if (!selectedDistrict) {
      outputSection.innerHTML = "";
      summarySection.style.display = "none";
      return;
    }

    renderDistrict(stateSelect.value, selectedDistrict);
  });

  function renderDistrict(state, district) {
    var constituencies = (stateNetwork[state] && stateNetwork[state][district]) ? stateNetwork[state][district] : [];
    var districtOnboarded = 0;

    constituencies.forEach(function (constituency) {
      var distributors = distributorData[constituency] || [];
      districtOnboarded += distributors.length;
    });

    var totalConstituencies = constituencies.length;
    var totalSeats = totalConstituencies * TOTAL_SEATS_PER_CONSTITUENCY;
    var availableSeats = totalSeats - districtOnboarded;

    document.getElementById("spDistrictTitle").textContent = district + " District, " + state;
    document.getElementById("spTotalConstituencies").textContent = totalConstituencies;
    document.getElementById("spTotalSeats").textContent = totalSeats;
    document.getElementById("spOnboardedSeats").textContent = districtOnboarded;
    document.getElementById("spAvailableSeats").textContent = availableSeats;

    summarySection.style.display = "block";
    outputSection.innerHTML = "";

    constituencies.forEach(function (constituency) {
      var distributors = distributorData[constituency] || [];
      var onboarded = distributors.length;
      var available = Math.max(TOTAL_SEATS_PER_CONSTITUENCY - onboarded, 0);
      var status = getConstituencyStatus(onboarded, available);

      var card = document.createElement("div");
      card.className = "sp-constituency-card";

      var distributorHtml = buildDistributorHtml(distributors);
      var actionButton = buildMainActionButton(available);

      card.innerHTML =
        '<div class="sp-constituency-top">' +
          '<div>' +
            '<h3>' + escapeHtml(constituency) + ' Constituency</h3>' +
          '</div>' +
          '<div class="sp-badge-row">' +
            '<span class="sp-badge">Total Seats: ' + TOTAL_SEATS_PER_CONSTITUENCY + '</span>' +
            '<span class="sp-badge">Onboarded: ' + onboarded + '</span>' +
            '<span class="sp-badge">Available: ' + available + '</span>' +
            '<span class="sp-badge ' + status.className + '">' + status.label + '</span>' +
          '</div>' +
        '</div>' +
        distributorHtml +
        '<div class="sp-action-row">' +
          actionButton +
          '<a href="' + contactPageUrl + '" class="sp-btn sp-btn-secondary">Talk to Source Pro Team</a>' +
        '</div>' +
        '<p class="sp-card-note">' +
          'Distributor details are displayed for local business verification and confidence-building purposes. Full details may be shared only as per company policy and distributor consent.' +
        '</p>';

      outputSection.appendChild(card);
    });
  }

  function buildDistributorHtml(distributors) {
    var html = "";

    if (!distributors || distributors.length === 0) {
      return (
        '<div class="sp-no-distributor">' +
          'No distributor has been onboarded in this constituency yet. This is an open opportunity for eligible applicants.' +
        '</div>'
      );
    }

    html += '<div class="sp-distributor-grid">';

    distributors.forEach(function (distributor) {
      var callButton = "";

      if (distributor.mobileLink && distributor.mobileLink !== "") {
        callButton =
          '<div class="sp-action-row">' +
            '<a class="sp-btn sp-btn-secondary" href="' + escapeAttribute(distributor.mobileLink) + '">Call Distributor</a>' +
          '</div>';
      }

      html +=
        '<div class="sp-distributor-card">' +
          '<img class="sp-distributor-photo" src="' + escapeAttribute(distributor.photo) + '" alt="' + escapeAttribute(distributor.name) + '">' +
          '<div class="sp-distributor-details">' +
            '<h4>' + escapeHtml(distributor.name) + '</h4>' +
            '<p><strong>Trade Name:</strong> ' + escapeHtml(distributor.tradeName) + '</p>' +
            '<p><strong>Location:</strong> ' + escapeHtml(distributor.addressDisplay) + '</p>' +
            '<p><strong>Mobile:</strong> ' + escapeHtml(distributor.mobileDisplay) + '</p>' +
            '<span class="sp-verified">' + escapeHtml(distributor.gstDisplay) + '</span>' +
            callButton +
          '</div>' +
        '</div>';
    });

    html += '</div>';

    return html;
  }

  function buildMainActionButton(available) {
    if (available > 0) {
      return '<a href="' + registrationPageUrl + '" class="sp-btn sp-btn-primary">Apply for Available Distributor Seat</a>';
    }

    return '<a href="' + registrationPageUrl + '" class="sp-btn sp-btn-secondary">Join Waiting List</a>';
  }

  function getConstituencyStatus(onboarded, available) {
    if (onboarded === 0) {
      return {
        label: "Applications Open",
        className: "sp-status-open"
      };
    }

    if (available > 0) {
      return {
        label: "Limited Seats Available",
        className: "sp-status-limited"
      };
    }

    return {
      label: "Currently Filled",
      className: "sp-status-filled"
    };
  }

  function escapeHtml(text) {
    if (text === null || text === undefined) {
      return "";
    }

    return String(text)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#039;");
  }

  function escapeAttribute(text) {
    return escapeHtml(text);
  }

  /*
    Optional:
    Auto-select Kerala on page load.
    Remove the next two lines if you do not want auto-selection.
  */
  stateSelect.value = "Kerala";
  stateSelect.dispatchEvent(new Event("change"));
});
