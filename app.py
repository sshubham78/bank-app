def generate_bank_statement(data):
    statement_template = f"""
    SBI Bank Statement
    
    Account Name          : {data['account_name']}
    Address               : S/O: {data['address']['father_name']}
                            {data['address']['ward']}
                            {data['address']['city']}-{data['address']['postal_code']}
                            {data['address']['state']}
    Date                  : {data['date']}
    Account Number        : {data['account_number']}
    Account Description   : {data['account_description']}
    Branch                : {data['branch']}
    Drawing Power         : {data['drawing_power']:.2f}
    Interest Rate (% p.a.): {data['interest_rate']}
    MOD Balance           : {data['mod_balance']:.2f}
    CIF No.               : {data['cif_no']}
    CKYCR Number          : {data['ckycr_number']}
    IFS Code              : {data['ifs_code']}
    MICR Code             : {data['micr_code']}
    Nomination Registered : {data['nomination_registered']}
    Balance as on {data['balance_as_on']['date']} : {data['balance_as_on']['amount']:,.2f}
    """
    return statement_template

# Example call with the above JSON data converted to Python dict
data = {
  "account_name": "Mr. RAJU",
  "address": {
    "father_name": "Jayprakash Rajput",
    "ward": "WARD 01 mehangipura",
    "city": "berasia",
    "postal_code": "462038",
    "state": "Bhopal"
  },
  "date": "17 Jan 2026",
  "account_number": "00000042511739493",
  "account_description": "SBCHQ-SGSP-PUBIND-DIAMOND-INR",
  "branch": "BERASIA MAIN ROAD",
  "drawing_power": 0.00,
  "interest_rate": 2.5,
  "mod_balance": 0.00,
  "cif_no": "67262931429",
  "ckycr_number": "XXXXXXXXXXX1234",
  "ifs_code": "SBIN0001499",
  "micr_code": "462002502",
  "nomination_registered": "No",
  "balance_as_on": {
    "date": "17 Jul 2025",
    "amount": 53256.00
  }
}

print(generate_bank_statement(data))
