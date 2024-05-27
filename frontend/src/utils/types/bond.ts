export interface creditInfo {
    credit_rating_sp: string,
    credit_rating_fitch: string,
    credit_rating_moody: string,
}

export interface bondType {
    annual_coupon_frequency: number,
    annual_coupon_rate: number,
    bond_type: number,
    coupon_dates: string[],
    coupon_type: number,
    credit_rating_sp: string,
    credit_rating_fitch: string,
    credit_rating_moody: string,
    currency: string,
    introduction: string,
    investor: number,
    is_callable: boolean,
    isin: string,
    issue_date: string,
    issue_datetime?: string,
    issue_name: string,
    issue_size: number,
    issuer: string,
    maturity_date: string,
    maturity_datetime?: string,
    minimum_investment_quantity: number,
    note: string,
    parent_company: string,
    parent_company_industry: string,
    seniority: number,
    guarantor: string,
    status: string,
    uid?: string,
}
export interface bondEditType {
    isin: string,
    credit_rating_fitch: string,
    credit_rating_moody: string,
    credit_rating_sp: string
    introduction: number,
    investor: string;
}