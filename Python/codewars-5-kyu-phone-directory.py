import re

def phone(s, num):
    a = s.split('\n')
    r = []
    for i in a:
        if i == "":
            continue
        phone = re.search(r'\d{1,2}-\d{3}-\d{3}-\d{4}', i).group(0)
        name = re.search(r"<[a-zA-z\s']+>", i).group(0)[1:-1]
        x = i.replace(phone, '').replace(name,'')
        y = re.sub(r'[<>;!/+?]', '',x)
        adress = re.sub(r'\s{2,}', ' ', y).replace(' , ', ' ').replace("$", '').replace("  ", " ").replace('_', ' ').replace('* ', '').replace(': ', '').replace(',', '').strip()
        print(f"Phone => {phone}, Name => {name}, Address => {adress}")
        if phone == num:
            r.append(f"Phone => {phone}, Name => {name}, Address => {adress}")
    if len(r) == 0:
        return f"Error => Not found: {num}"
    elif len(r) > 1:
        return f"Error => Too many people: {num}"
    return r[0]


s = ("/+1-541-754-3010 156 Alphand_St. <J Steeve>\n 133, Green, Rd. <E Kustur> NY-56423 ;+1-541-914-3010;\n"
        "+1-541-984-3012 <P Reed> /PO Box 530; Pollocksville, NC-28573\n :+1-321-512-2222 <Paul Dive> Sequoia Alley PQ-67209\n"
        "+1-741-984-3090 <Peter Reedgrave> _Chicago\n :+1-921-333-2222 <Anna Stevens> Haramburu_Street AA-67209\n"
        "+1-111-544-8973 <Peter Pan> LA\n +1-921-512-2222 <Wilfrid Stevens> Wild Street AA-67209\n"
        "<Peter Gone> LA ?+1-121-544-8974 \n <R Steell> Quora Street AB-47209 +1-481-512-2222!\n"
        "<Arthur Clarke> San Antonio $+1-121-504-8974 TT-45120\n <Ray Chandler> Teliman Pk. !+1-681-512-2222! AB-47209,\n"
        "<Sophia Loren> +1-421-674-8974 Bern TP-46017\n <Peter O'Brien> High Street +1-908-512-2222; CC-47209\n"
        "<Anastasia> +48-421-674-8974 Via Quirinal Roma\n <P Salinger> Main Street, +1-098-512-2222, Denver\n"
        "<C Powel> *+19-421-674-8974 Chateau des Fosses Strasbourg F-68000\n <Bernard Deltheil> +1-498-512-2222; Mount Av.  Eldorado\n"
        "+1-099-500-8000 <Peter Crush> Labrador Bd.\n +1-931-512-4855 <William Saurin> Bison Street CQ-23071\n"
        "<P Salinge> Main Street, +1-098-512-2222, Denve\n")
print(phone(s, "48-421-674-8974"))