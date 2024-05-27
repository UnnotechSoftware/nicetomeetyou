export interface registerType {
    name: string,
    email: string,
    password: string,
    password2: string,
    identity: string
}
export interface resetPasswordType {
    new_password: string,
    new_password_confirm: string,
}
export interface forgetPasswordType {
    email: string,
    group_name: string,
}

export interface registerRulesType {
    name: ({
        required: boolean;
        message: string;
        trigger: string;
    } | {
        min: number;
        max: number;
        message: string;
        trigger: string;
    })[];
    email: {
        type: string;
        required: boolean;
        message: string;
        trigger: string;
    }[];
    password: ({
        required: boolean;
        message: string;
        trigger: string;
    } | {
        min: number;
        max: number;
        message: string;
        trigger: string;
    })[];
    password2: ({
        required: boolean;
        message: string;
        trigger: string;
    } | {
        min: number;
        max: number;
        message: string;
        trigger: string;
    } | {
        validator: (rule: any, value: string, callback: any) => void,
        trigger: string
    })[];
}

export interface loginType {
    email: string,
    password: string,
}

export interface loginRulesType {
    email: {
        type: string;
        required: boolean;
        message: string;
        trigger: string;
    }[];
    password: ({
        required: boolean;
        message: string;
        trigger: string;
    } | {
        min: number;
        max: number;
        message: string;
        trigger: string;
    })[];
}

export interface userType {
    exp?: number;
    user_id: string;
    full_name: string,
}

export interface formDataType {
    type: string;
    describe: string;
    income: string;
    expend: string;
    cash: string;
    remark: string;
    _id?: string | undefined
}


export interface formRulesType {
    describe: {
        required: boolean,
        message: string,
        trigger: string[]
    }[],
    income: {
        required: boolean,
        message: string,
        trigger: string[]
    }[],
    expend: {
        required: boolean,
        message: string,
        trigger: string[]
    }[],
    cash: {
        required: boolean,
        message: string,
        trigger: string[]
    }[]
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
    issue_name: string,
    issue_size: number,
    issuer: string,
    maturity_date: string,
    minimum_investment_quantity: number,
    note: string,
    parent_company: string,
    parent_company_industry: string,
    seniority: number,
    guarantor: string,
    uid?: string
}