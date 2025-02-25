def calculate_lcr(hqla, net_cash_outflows):
    if net_cash_outflows == 0:
        return "Net Cash Outflows cannot be zero!"
    return round((hqla / net_cash_outflows) * 100, 2)

def calculate_nsfr(asf, rsf):
    if rsf == 0:
        return "Required Stable Funding (RSF) cannot be zero!"
    return round((asf / rsf) * 100, 2)

print("Liquidity Coverage Ratio (LCR) & Net Stable Funding Ratio (NSFR) Calculator")
hqla = float(input("Enter High-Quality Liquid Assets (HQLA): "))
net_cash_outflows = float(input("Enter Net Cash Outflows over 30 days: "))
asf = float(input("Enter Available Stable Funding (ASF): "))
rsf = float(input("Enter Required Stable Funding (RSF): "))

lcr_result = calculate_lcr(hqla, net_cash_outflows)
nsfr_result = calculate_nsfr(asf, rsf)

print("\nResults:")
print(f"LCR: {lcr_result}%")
print(f"NSFR: {nsfr_result}%")

if isinstance(lcr_result, float) and lcr_result >= 100:
    print("✅ LCR is compliant with Basel III.")
else:
    print("⚠️ LCR is below 100%. Increase HQLA or reduce net cash outflows.")

if isinstance(nsfr_result, float) and nsfr_result >= 100:
    print("✅ NSFR is compliant with Basel III.")
else:
    print("⚠️ NSFR is below 100%. Increase ASF or reduce RSF.")
