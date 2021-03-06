from app.extensions.init_sqlalchemy import db


class Cashflow(db.Model):
    __tablename__ = 'cash_flow'
    id = db.Column(db.Integer, primary_key=True, comment='现金流量表编号')
    ts_code = db.Column(db.String(255), comment='TS股票代码')
    ann_date = db.Column(db.String(255), comment='公告日期')
    f_ann_date = db.Column(db.String(255), comment='实际公告日期')
    end_date = db.Column(db.String(255), comment='报告期')
    report_type = db.Column(db.String(255), comment='报表类型')
    end_type = db.Column(db.String(255), comment='报告期类型')
    net_profit = db.Column(db.Float, comment='净利润')
    finan_exp = db.Column(db.Float, comment='财务费用')
    c_fr_sale_sg = db.Column(db.Float, comment='销售商品、提供劳务收到的现金')
    recp_tax_rends = db.Column(db.Float, comment='收到的税费返还')
    n_depos_incr_fi = db.Column(db.Float, comment='客户存款和同业存放款项净增加额')
    n_incr_loans_cb = db.Column(db.Float, comment='向中央银行借款净增加额')
    n_inc_borr_oth_fi = db.Column(db.Float, comment='向其他金融机构拆入资金净增加额')
    prem_fr_orig_contr = db.Column(db.Float, comment='收到原保险合同保费取得的现金')
    n_incr_insured_dep = db.Column(db.Float, comment='保户储金净增加额')
    n_reinsur_prem = db.Column(db.Float, comment='收到再保业务现金净额')
    n_incr_disp_tfa = db.Column(db.Float, comment='处置交易性金融资产净增加额')
    ifc_cash_incr = db.Column(db.Float, comment='收取利息和手续费净增加额')
    n_incr_disp_faas = db.Column(db.Float, comment='处置可供出售金融资产净增加额')
    n_incr_loans_oth_bank = db.Column(db.Float, comment='拆入资金净增加额')
    n_cap_incr_repur = db.Column(db.Float, comment='回购业务资金净增加额')
    c_fr_oth_operate_a = db.Column(db.Float, comment='收到其他与经营活动有关的现金')
    c_inf_fr_operate_a = db.Column(db.Float, comment='经营活动现金流入小计')
    c_paid_goods_s = db.Column(db.Float, comment='购买商品、接受劳务支付的现金')
    c_paid_to_for_empl = db.Column(db.Float, comment='支付给职工以及为职工支付的现金')
    c_paid_for_taxes = db.Column(db.Float, comment='支付的各项税费')
    n_incr_clt_loan_adv = db.Column(db.Float, comment='客户贷款及垫款净增加额')
    n_incr_dep_cbob = db.Column(db.Float, comment='存放央行和同业款项净增加额')
    c_pay_claims_orig_inco = db.Column(db.Float, comment='支付原保险合同赔付款项的现金')
    pay_handling_chrg = db.Column(db.Float, comment='支付手续费的现金')
    pay_comm_insur_plcy = db.Column(db.Float, comment='支付保单红利的现金')
    oth_cash_pay_oper_act = db.Column(db.Float, comment='支付其他与经营活动有关的现金')
    st_cash_out_act = db.Column(db.Float, comment='经营活动现金流出小计')
    n_cashflow_act = db.Column(db.Float, comment='经营活动产生的现金流量净额')
    oth_recp_ral_inv_act = db.Column(db.Float, comment='收到其他与投资活动有关的现金')
    c_disp_withdrwl_invest = db.Column(db.Float, comment='收回投资收到的现金')
    c_recp_return_invest = db.Column(db.Float, comment='取得投资收益收到的现金')
    n_recp_disp_fiolta = db.Column(db.Float,
                                   comment='处置固定资产、无形资产和其他长期资产收回的现金净额')
    n_recp_disp_sobu = db.Column(db.Float, comment='处置子公司及其他营业单位收到的现金净额')
    stot_inflows_inv_act = db.Column(db.Float, comment='投资活动现金流入小计')
    c_pay_acq_const_fiolta = db.Column(db.Float,
                                       comment='购建固定资产、无形资产和其他长期资产支付的现金')
    c_paid_invest = db.Column(db.Float, comment='投资支付的现金')
    n_disp_subs_oth_biz = db.Column(db.Float, comment='取得子公司及其他营业单位支付的现金净额')
    oth_pay_ral_inv_act = db.Column(db.Float, comment='支付其他与投资活动有关的现金')
    n_incr_pledge_loan = db.Column(db.Float, comment='质押贷款净增加额')
    stot_out_inv_act = db.Column(db.Float, comment='投资活动现金流出小计')
    n_cashflow_inv_act = db.Column(db.Float, comment='投资活动产生的现金流量净额')
    c_recp_borrow = db.Column(db.Float, comment='取得借款收到的现金')
    proc_issue_bonds = db.Column(db.Float, comment='发行债券收到的现金')
    oth_cash_recp_ral_fnc_act = db.Column(db.Float, comment='收到其他与筹资活动有关的现金')
    stot_cash_in_fnc_act = db.Column(db.Float, comment='筹资活动现金流入小计')
    free_cashflow = db.Column(db.Float, comment='企业自由现金流量')
    c_prepay_amt_borr = db.Column(db.Float, comment='偿还债务支付的现金')
    c_pay_dist_dpcp_int_exp = db.Column(db.Float, comment='分配股利、利润或偿付利息支付的现金')
    incl_dvd_profit_paid_sc_ms = db.Column(db.Float,
                                           comment='其中:子公司支付给少数股东的股利、利润')
    oth_cashpay_ral_fnc_act = db.Column(db.Float, comment='支付其他与筹资活动有关的现金')
    stot_cashout_fnc_act = db.Column(db.Float, comment='筹资活动现金流出小计')
    n_cash_flows_fnc_act = db.Column(db.Float, comment='筹资活动产生的现金流量净额')
    eff_fx_flu_cash = db.Column(db.Float, comment='汇率变动对现金的影响')
    n_incr_cash_cash_equ = db.Column(db.Float, comment='现金及现金等价物净增加额')
    c_cash_equ_beg_period = db.Column(db.Float, comment='期初现金及现金等价物余额')
    c_cash_equ_end_period = db.Column(db.Float, comment='期末现金及现金等价物余额')
    c_recp_cap_contrib = db.Column(db.Float, comment='吸收投资收到的现金')
    incl_cash_rec_saims = db.Column(db.Float, comment='其中:子公司吸收少数股东投资收到的现金')
    uncon_invest_loss = db.Column(db.Float, comment='未确认投资损失')
    prov_depr_assets = db.Column(db.Float, comment='加:资产减值准备')
    depr_fa_coga_dpba = db.Column(db.Float, comment='固定资产折旧、油气资产折耗、生产性生物资产折旧')
    amort_intang_assets = db.Column(db.Float, comment='无形资产摊销')
    lt_amort_deferred_exp = db.Column(db.Float, comment='长期待摊费用摊销')
    decr_deferred_exp = db.Column(db.Float, comment='待摊费用减少')
    incr_acc_exp = db.Column(db.Float, comment='预提费用增加')
    loss_disp_fiolta = db.Column(db.Float, comment='处置固定、无形资产和其他长期资产的损失')
    loss_scr_fa = db.Column(db.Float, comment='固定资产报废损失')
    loss_fv_chg = db.Column(db.Float, comment='公允价值变动损失')
    invest_loss = db.Column(db.Float, comment='投资损失')
    decr_def_inc_tax_assets = db.Column(db.Float, comment='递延所得税资产减少')
    incr_def_inc_tax_liab = db.Column(db.Float, comment='递延所得税负债增加')
    decr_inventories = db.Column(db.Float, comment='存货的减少')
    decr_oper_payable = db.Column(db.Float, comment='经营性应收项目的减少')
    incr_oper_payable = db.Column(db.Float, comment='经营性应付项目的增加')
    others = db.Column(db.Float, comment='其他')
    im_net_cashflow_oper_act = db.Column(db.Float,
                                         comment='经营活动产生的现金流量净额(间接法)')
    conv_debt_into_cap = db.Column(db.Float, comment='债务转为资本')
    conv_copbonds_due_within_1y = db.Column(db.Float, comment='一年内到期的可转换公司债券')
    fa_fnc_leases = db.Column(db.Float, comment='融资租入固定资产')
    im_n_incr_cash_equ = db.Column(db.Float, comment='现金及现金等价物净增加额(间接法)')
    net_dism_capital_add = db.Column(db.Float, comment='拆出资金净增加额')
    net_cash_rece_sec = db.Column(db.Float, comment='代理买卖证券收到的现金净额(元)')
    credit_impa_loss = db.Column(db.Float, comment='信用减值损失')
    use_right_asset_dep = db.Column(db.Float, comment='使用权资产折旧')
    oth_loss_asset = db.Column(db.Float, comment='其他资产减值损失')
    end_bal_cash = db.Column(db.Float, comment='现金的期末余额')
    beg_bal_cash = db.Column(db.Float, comment='减:现金的期初余额')
    end_bal_cash_equ = db.Column(db.Float, comment='加:现金等价物的期末余额')
    beg_bal_cash_equ = db.Column(db.Float, comment='减:现金等价物的期初余额')
    update_flag = db.Column(db.Float, comment='更新标志(1最新）')