export interface bondRulesType {
    annual_coupon_rate: { message: string; required: boolean }[];
    credit_rating_fitch: { message: string; required: boolean }[];
    credit_rating_moody: { message: string; required: boolean }[];
    credit_rating_sp: { message: string; required: boolean }[];
    issue_size: { message: string; required: boolean }[];
    is_callable: { message: string; required: boolean }[];
    parent_company: { message: string; required: boolean }[];
    maturity_date: { message: string; required: boolean }[];
    guarantor: { message: string; required: boolean }[];
    minimum_investment_quantity: { message: string; required: boolean }[];
    issuer: { message: string; required: boolean }[];
    bond_type: { message: string; required: boolean }[];
    annual_coupon_frequency: { message: string; required: boolean }[];
    investor: { message: string; required: boolean }[];
    issue_name: { message: string; required: boolean }[];
    parent_company_industry: { message: string; required: boolean }[];
    issue_date: { message: string; required: boolean }[];
    coupon_dates: { message: string; required: boolean }[];
    currency: { message: string; required: boolean }[];
    isin: { message: string; required: boolean }[];
    seniority: { message: string; required: boolean }[];
    coupon_type: { message: string; required: boolean }[];
    introduction: { message: string; required: boolean }[];
    bond_contract_type: {message: string; required: boolean}[];
    country_code: {message: string; required: boolean}[];
}
export interface boundEditRulesType {
    isin: { message: string; required: boolean }[];
    credit_rating_fitch: { message: string; required: boolean }[];
    credit_rating_moody: { message: string; required: boolean }[];
    credit_rating_sp: { message: string; required: boolean }[];
    introduction: { message: string; required: boolean }[];
    investor: { message: string; required: boolean }[];
}

export interface bondManageEditRulesType {
    isin: { message: string; required: boolean }[];
    trust_management_fee_rate: {message: string; required: boolean}[];
    handling_fee_rate: {message: string; required: boolean}[];
    ask_price: {message: string; required: boolean}[];
    bid_price: {message: string; required: boolean}[];
    ytm: {message: string; required: boolean}[];
}