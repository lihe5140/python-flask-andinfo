"""empty message

Revision ID: ce4dbf0e64e3
Revises: 
Create Date: 2021-12-31 10:57:07.431503

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ce4dbf0e64e3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('balance_sheet',
    sa.Column('id', sa.Integer(), nullable=False, comment='负债表编号'),
    sa.Column('ts_code', sa.String(length=255), nullable=True, comment='TS股票代码'),
    sa.Column('ann_date', sa.String(length=255), nullable=True, comment='公告日期'),
    sa.Column('f_ann_date', sa.String(length=255), nullable=True, comment='实际公告日期'),
    sa.Column('end_date', sa.String(length=255), nullable=True, comment='报告期'),
    sa.Column('report_type', sa.String(length=255), nullable=True, comment='报表类型'),
    sa.Column('comp_type', sa.String(length=255), nullable=True, comment='公司类型'),
    sa.Column('total_share', sa.Float(), nullable=True, comment='期末总股本'),
    sa.Column('cap_rese', sa.Float(), nullable=True, comment='资本公积金'),
    sa.Column('undistr_porfit', sa.Float(), nullable=True, comment='未分配利润'),
    sa.Column('surplus_rese', sa.Float(), nullable=True, comment='盈余公积金'),
    sa.Column('special_rese', sa.Float(), nullable=True, comment='专项储备'),
    sa.Column('money_cap', sa.Float(), nullable=True, comment='货币资金'),
    sa.Column('trad_asset', sa.Float(), nullable=True, comment='交易性金融资产'),
    sa.Column('notes_receiv', sa.Float(), nullable=True, comment='应收票据'),
    sa.Column('accounts_receiv', sa.Float(), nullable=True, comment='应收账款'),
    sa.Column('oth_receiv', sa.Float(), nullable=True, comment='其他应收款'),
    sa.Column('prepayment', sa.Float(), nullable=True, comment='预付款项'),
    sa.Column('div_receiv', sa.Float(), nullable=True, comment='应收股利'),
    sa.Column('int_receiv', sa.Float(), nullable=True, comment='应收利息'),
    sa.Column('inventories', sa.Float(), nullable=True, comment='存货'),
    sa.Column('amor_exp', sa.Float(), nullable=True, comment='待摊费用'),
    sa.Column('nca_within_1y', sa.Float(), nullable=True, comment='一年内到期的非流动资产'),
    sa.Column('sett_rsrv', sa.Float(), nullable=True, comment='结算备付金'),
    sa.Column('loanto_oth_bank_fi', sa.Float(), nullable=True, comment='拆出资金'),
    sa.Column('premium_receiv', sa.Float(), nullable=True, comment='应收保费'),
    sa.Column('reinsur_receiv', sa.Float(), nullable=True, comment='应收分保账款'),
    sa.Column('reinsur_res_receiv', sa.Float(), nullable=True, comment='应收分保合同准备金'),
    sa.Column('pur_resale_fa', sa.Float(), nullable=True, comment='买入返售金融资产'),
    sa.Column('oth_cur_assets', sa.Float(), nullable=True, comment='其他流动资产'),
    sa.Column('total_cur_assets', sa.Float(), nullable=True, comment='流动资产合计'),
    sa.Column('fa_avail_for_sale', sa.Float(), nullable=True, comment='可供出售金融资产'),
    sa.Column('htm_invest', sa.Float(), nullable=True, comment='持有至到期投资'),
    sa.Column('lt_eqt_invest', sa.Float(), nullable=True, comment='长期股权投资'),
    sa.Column('invest_real_estate', sa.Float(), nullable=True, comment='投资性房地产'),
    sa.Column('time_deposits', sa.Float(), nullable=True, comment='定期存款'),
    sa.Column('oth_assets', sa.Float(), nullable=True, comment='其他资产'),
    sa.Column('lt_rec', sa.Float(), nullable=True, comment='长期应收款'),
    sa.Column('fix_assets', sa.Float(), nullable=True, comment='固定资产'),
    sa.Column('cip', sa.Float(), nullable=True, comment='在建工程'),
    sa.Column('const_materials', sa.Float(), nullable=True, comment='工程物资'),
    sa.Column('fixed_assets_disp', sa.Float(), nullable=True, comment='固定资产清理'),
    sa.Column('produc_bio_assets', sa.Float(), nullable=True, comment='生产性生物资产'),
    sa.Column('oil_and_gas_assets', sa.Float(), nullable=True, comment='油气资产'),
    sa.Column('intan_assets', sa.Float(), nullable=True, comment='无形资产'),
    sa.Column('r_and_d', sa.Float(), nullable=True, comment='研发支出'),
    sa.Column('goodwill', sa.Float(), nullable=True, comment='商誉'),
    sa.Column('lt_amor_exp', sa.Float(), nullable=True, comment='长期待摊费用'),
    sa.Column('defer_tax_assets', sa.Float(), nullable=True, comment='递延所得税资产'),
    sa.Column('decr_in_disbur', sa.Float(), nullable=True, comment='发放贷款及垫款'),
    sa.Column('oth_nca', sa.Float(), nullable=True, comment='其他非流动资产'),
    sa.Column('total_nca', sa.Float(), nullable=True, comment='非流动资产合计'),
    sa.Column('cash_reser_cb', sa.Float(), nullable=True, comment='现金及存放中央银行款项'),
    sa.Column('depos_in_oth_bfi', sa.Float(), nullable=True, comment='存放同业和其它金融机构款项'),
    sa.Column('prec_metals', sa.Float(), nullable=True, comment='贵金属'),
    sa.Column('deriv_assets', sa.Float(), nullable=True, comment='\t衍生金融资产'),
    sa.Column('rr_reins_une_prem', sa.Float(), nullable=True, comment='应收分保未到期责任准备金'),
    sa.Column('rr_reins_outstd_cla', sa.Float(), nullable=True, comment='应收分保未决赔款准备金'),
    sa.Column('rr_reins_lins_liab', sa.Float(), nullable=True, comment='应收分保寿险责任准备金'),
    sa.Column('rr_reins_lthins_liab', sa.Float(), nullable=True, comment='应收分保长期健康险责任准备金'),
    sa.Column('refund_depos', sa.Float(), nullable=True, comment='存出保证金'),
    sa.Column('ph_pledge_loans', sa.Float(), nullable=True, comment='保户质押贷款'),
    sa.Column('refund_cap_depos', sa.Float(), nullable=True, comment='存出资本保证金'),
    sa.Column('indep_acct_assets', sa.Float(), nullable=True, comment='独立账户资产'),
    sa.Column('client_depos', sa.Float(), nullable=True, comment='其中：客户资金存款'),
    sa.Column('client_prov', sa.Float(), nullable=True, comment='其中：客户备付金'),
    sa.Column('transac_seat_fee', sa.Float(), nullable=True, comment='其中:交易席位费'),
    sa.Column('invest_as_receiv', sa.Float(), nullable=True, comment='应收款项类投资'),
    sa.Column('total_assets', sa.Float(), nullable=True, comment='资产总计'),
    sa.Column('lt_borr', sa.Float(), nullable=True, comment='长期借款'),
    sa.Column('st_borr', sa.Float(), nullable=True, comment='短期借款'),
    sa.Column('cb_borr', sa.Float(), nullable=True, comment='向中央银行借款'),
    sa.Column('depos_ib_deposits', sa.Float(), nullable=True, comment='吸收存款及同业存放'),
    sa.Column('loan_oth_bank', sa.Float(), nullable=True, comment='拆入资金'),
    sa.Column('trading_fl', sa.Float(), nullable=True, comment='交易性金融负债'),
    sa.Column('notes_payable', sa.Float(), nullable=True, comment='应付票据'),
    sa.Column('acct_payable', sa.Float(), nullable=True, comment='应付账款'),
    sa.Column('adv_receipts', sa.Float(), nullable=True, comment='预收款项'),
    sa.Column('sold_for_repur_fa', sa.Float(), nullable=True, comment='卖出回购金融资产款'),
    sa.Column('comm_payable', sa.Float(), nullable=True, comment='应付手续费及佣金'),
    sa.Column('payroll_payable', sa.Float(), nullable=True, comment='应付职工薪酬'),
    sa.Column('taxes_payable', sa.Float(), nullable=True, comment='应交税费'),
    sa.Column('int_payable', sa.Float(), nullable=True, comment='应付利息'),
    sa.Column('div_payable', sa.Float(), nullable=True, comment='应付股利'),
    sa.Column('oth_payable', sa.Float(), nullable=True, comment='其他应付款'),
    sa.Column('acc_exp', sa.Float(), nullable=True, comment='预提费用'),
    sa.Column('deferred_inc', sa.Float(), nullable=True, comment='递延收益'),
    sa.Column('st_bonds_payable', sa.Float(), nullable=True, comment='应付短期债券'),
    sa.Column('payable_to_reinsurer', sa.Float(), nullable=True, comment='应付分保账款'),
    sa.Column('rsrv_insur_cont', sa.Float(), nullable=True, comment='保险合同准备金'),
    sa.Column('acting_trading_sec', sa.Float(), nullable=True, comment='代理买卖证券款'),
    sa.Column('acting_uw_sec', sa.Float(), nullable=True, comment='代理承销证券款'),
    sa.Column('non_cur_liab_due_1y', sa.Float(), nullable=True, comment='一年内到期的非流动负债'),
    sa.Column('oth_cur_liab', sa.Float(), nullable=True, comment='其他流动负债'),
    sa.Column('total_cur_liab', sa.Float(), nullable=True, comment='流动负债合计'),
    sa.Column('bond_payable', sa.Float(), nullable=True, comment='应付债券'),
    sa.Column('lt_payable', sa.Float(), nullable=True, comment='长期应付款'),
    sa.Column('specific_payables', sa.Float(), nullable=True, comment='专项应付款'),
    sa.Column('estimated_liab', sa.Float(), nullable=True, comment='预计负债'),
    sa.Column('defer_tax_liab', sa.Float(), nullable=True, comment='递延所得税负债'),
    sa.Column('defer_inc_non_cur_liab', sa.Float(), nullable=True, comment='递延收益-非流动负债'),
    sa.Column('oth_ncl', sa.Float(), nullable=True, comment='其他非流动负债'),
    sa.Column('total_ncl', sa.Float(), nullable=True, comment='非流动负债合计'),
    sa.Column('depos_oth_bfi', sa.Float(), nullable=True, comment='同业和其它金融机构存放款项'),
    sa.Column('deriv_liab', sa.Float(), nullable=True, comment='衍生金融负债'),
    sa.Column('depos', sa.Float(), nullable=True, comment='吸收存款'),
    sa.Column('agency_bus_liab', sa.Float(), nullable=True, comment='代理业务负债'),
    sa.Column('oth_liab', sa.Float(), nullable=True, comment='其他负债'),
    sa.Column('prem_receiv_adva', sa.Float(), nullable=True, comment='预收保费'),
    sa.Column('depos_received', sa.Float(), nullable=True, comment='存入保证金'),
    sa.Column('ph_invest', sa.Float(), nullable=True, comment='保户储金及投资款'),
    sa.Column('reser_une_prem', sa.Float(), nullable=True, comment='未到期责任准备金'),
    sa.Column('reser_outstd_claims', sa.Float(), nullable=True, comment='未决赔款准备金'),
    sa.Column('reser_lins_liab', sa.Float(), nullable=True, comment='寿险责任准备金'),
    sa.Column('reser_lthins_liab', sa.Float(), nullable=True, comment='长期健康险责任准备金'),
    sa.Column('indept_acc_liab', sa.Float(), nullable=True, comment='独立账户负债'),
    sa.Column('pledge_borr', sa.Float(), nullable=True, comment='其中:质押借款'),
    sa.Column('indem_payable', sa.Float(), nullable=True, comment='应付赔付款'),
    sa.Column('policy_div_payable', sa.Float(), nullable=True, comment='应付保单红利'),
    sa.Column('total_liab', sa.Float(), nullable=True, comment='负债合计'),
    sa.Column('treasury_share', sa.Float(), nullable=True, comment='减:库存股'),
    sa.Column('ordin_risk_reser', sa.Float(), nullable=True, comment='一般风险准备'),
    sa.Column('forex_differ', sa.Float(), nullable=True, comment='外币报表折算差额'),
    sa.Column('invest_loss_unconf', sa.Float(), nullable=True, comment='未确认的投资损失'),
    sa.Column('minority_int', sa.Float(), nullable=True, comment='少数股东权益'),
    sa.Column('total_hldr_eqy_exc_min_int', sa.Float(), nullable=True, comment='股东权益合计(不含少数股东权益)'),
    sa.Column('total_hldr_eqy_inc_min_int', sa.Float(), nullable=True, comment='股东权益合计(含少数股东权益)'),
    sa.Column('total_liab_hldr_eqy', sa.Float(), nullable=True, comment='负债及股东权益总计'),
    sa.Column('lt_payroll_payable', sa.Float(), nullable=True, comment='长期应付职工薪酬'),
    sa.Column('oth_comp_income', sa.Float(), nullable=True, comment='其他综合收益'),
    sa.Column('oth_eqt_tools', sa.Float(), nullable=True, comment='其他权益工具'),
    sa.Column('oth_eqt_tools_p_shr', sa.Float(), nullable=True, comment='其他权益工具(优先股)'),
    sa.Column('lending_funds', sa.Float(), nullable=True, comment='融出资金'),
    sa.Column('acc_receivable', sa.Float(), nullable=True, comment='应收款项'),
    sa.Column('st_fin_payable', sa.Float(), nullable=True, comment='应付短期融资款'),
    sa.Column('payables', sa.Float(), nullable=True, comment='应付款项'),
    sa.Column('hfs_assets', sa.Float(), nullable=True, comment='持有待售的资产'),
    sa.Column('hfs_sales', sa.Float(), nullable=True, comment='持有待售的负债'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cash_flow',
    sa.Column('id', sa.Integer(), nullable=False, comment='现金流量表编号'),
    sa.Column('ts_code', sa.String(length=255), nullable=True, comment='TS股票代码'),
    sa.Column('ann_date', sa.String(length=255), nullable=True, comment='公告日期'),
    sa.Column('f_ann_date', sa.String(length=255), nullable=True, comment='实际公告日期'),
    sa.Column('end_date', sa.String(length=255), nullable=True, comment='报告期'),
    sa.Column('report_type', sa.String(length=255), nullable=True, comment='报表类型'),
    sa.Column('end_type', sa.String(length=255), nullable=True, comment='报告期类型'),
    sa.Column('net_profit', sa.Float(), nullable=True, comment='净利润'),
    sa.Column('finan_exp', sa.Float(), nullable=True, comment='财务费用'),
    sa.Column('c_fr_sale_sg', sa.Float(), nullable=True, comment='销售商品、提供劳务收到的现金'),
    sa.Column('recp_tax_rends', sa.Float(), nullable=True, comment='收到的税费返还'),
    sa.Column('n_depos_incr_fi', sa.Float(), nullable=True, comment='客户存款和同业存放款项净增加额'),
    sa.Column('n_incr_loans_cb', sa.Float(), nullable=True, comment='向中央银行借款净增加额'),
    sa.Column('n_inc_borr_oth_fi', sa.Float(), nullable=True, comment='向其他金融机构拆入资金净增加额'),
    sa.Column('prem_fr_orig_contr', sa.Float(), nullable=True, comment='收到原保险合同保费取得的现金'),
    sa.Column('n_incr_insured_dep', sa.Float(), nullable=True, comment='保户储金净增加额'),
    sa.Column('n_reinsur_prem', sa.Float(), nullable=True, comment='收到再保业务现金净额'),
    sa.Column('n_incr_disp_tfa', sa.Float(), nullable=True, comment='处置交易性金融资产净增加额'),
    sa.Column('ifc_cash_incr', sa.Float(), nullable=True, comment='收取利息和手续费净增加额'),
    sa.Column('n_incr_disp_faas', sa.Float(), nullable=True, comment='处置可供出售金融资产净增加额'),
    sa.Column('n_incr_loans_oth_bank', sa.Float(), nullable=True, comment='拆入资金净增加额'),
    sa.Column('n_cap_incr_repur', sa.Float(), nullable=True, comment='回购业务资金净增加额'),
    sa.Column('c_fr_oth_operate_a', sa.Float(), nullable=True, comment='收到其他与经营活动有关的现金'),
    sa.Column('c_inf_fr_operate_a', sa.Float(), nullable=True, comment='经营活动现金流入小计'),
    sa.Column('c_paid_goods_s', sa.Float(), nullable=True, comment='购买商品、接受劳务支付的现金'),
    sa.Column('c_paid_to_for_empl', sa.Float(), nullable=True, comment='支付给职工以及为职工支付的现金'),
    sa.Column('c_paid_for_taxes', sa.Float(), nullable=True, comment='支付的各项税费'),
    sa.Column('n_incr_clt_loan_adv', sa.Float(), nullable=True, comment='客户贷款及垫款净增加额'),
    sa.Column('n_incr_dep_cbob', sa.Float(), nullable=True, comment='存放央行和同业款项净增加额'),
    sa.Column('c_pay_claims_orig_inco', sa.Float(), nullable=True, comment='支付原保险合同赔付款项的现金'),
    sa.Column('pay_handling_chrg', sa.Float(), nullable=True, comment='支付手续费的现金'),
    sa.Column('pay_comm_insur_plcy', sa.Float(), nullable=True, comment='支付保单红利的现金'),
    sa.Column('oth_cash_pay_oper_act', sa.Float(), nullable=True, comment='支付其他与经营活动有关的现金'),
    sa.Column('st_cash_out_act', sa.Float(), nullable=True, comment='经营活动现金流出小计'),
    sa.Column('n_cashflow_act', sa.Float(), nullable=True, comment='经营活动产生的现金流量净额'),
    sa.Column('oth_recp_ral_inv_act', sa.Float(), nullable=True, comment='收到其他与投资活动有关的现金'),
    sa.Column('c_disp_withdrwl_invest', sa.Float(), nullable=True, comment='收回投资收到的现金'),
    sa.Column('c_recp_return_invest', sa.Float(), nullable=True, comment='取得投资收益收到的现金'),
    sa.Column('n_recp_disp_fiolta', sa.Float(), nullable=True, comment='处置固定资产、无形资产和其他长期资产收回的现金净额'),
    sa.Column('n_recp_disp_sobu', sa.Float(), nullable=True, comment='处置子公司及其他营业单位收到的现金净额'),
    sa.Column('stot_inflows_inv_act', sa.Float(), nullable=True, comment='投资活动现金流入小计'),
    sa.Column('c_pay_acq_const_fiolta', sa.Float(), nullable=True, comment='购建固定资产、无形资产和其他长期资产支付的现金'),
    sa.Column('c_paid_invest', sa.Float(), nullable=True, comment='投资支付的现金'),
    sa.Column('n_disp_subs_oth_biz', sa.Float(), nullable=True, comment='取得子公司及其他营业单位支付的现金净额'),
    sa.Column('oth_pay_ral_inv_act', sa.Float(), nullable=True, comment='支付其他与投资活动有关的现金'),
    sa.Column('n_incr_pledge_loan', sa.Float(), nullable=True, comment='质押贷款净增加额'),
    sa.Column('stot_out_inv_act', sa.Float(), nullable=True, comment='投资活动现金流出小计'),
    sa.Column('n_cashflow_inv_act', sa.Float(), nullable=True, comment='投资活动产生的现金流量净额'),
    sa.Column('c_recp_borrow', sa.Float(), nullable=True, comment='取得借款收到的现金'),
    sa.Column('proc_issue_bonds', sa.Float(), nullable=True, comment='发行债券收到的现金'),
    sa.Column('oth_cash_recp_ral_fnc_act', sa.Float(), nullable=True, comment='收到其他与筹资活动有关的现金'),
    sa.Column('stot_cash_in_fnc_act', sa.Float(), nullable=True, comment='筹资活动现金流入小计'),
    sa.Column('free_cashflow', sa.Float(), nullable=True, comment='企业自由现金流量'),
    sa.Column('c_prepay_amt_borr', sa.Float(), nullable=True, comment='偿还债务支付的现金'),
    sa.Column('c_pay_dist_dpcp_int_exp', sa.Float(), nullable=True, comment='分配股利、利润或偿付利息支付的现金'),
    sa.Column('incl_dvd_profit_paid_sc_ms', sa.Float(), nullable=True, comment='其中:子公司支付给少数股东的股利、利润'),
    sa.Column('oth_cashpay_ral_fnc_act', sa.Float(), nullable=True, comment='支付其他与筹资活动有关的现金'),
    sa.Column('stot_cashout_fnc_act', sa.Float(), nullable=True, comment='筹资活动现金流出小计'),
    sa.Column('n_cash_flows_fnc_act', sa.Float(), nullable=True, comment='筹资活动产生的现金流量净额'),
    sa.Column('eff_fx_flu_cash', sa.Float(), nullable=True, comment='汇率变动对现金的影响'),
    sa.Column('n_incr_cash_cash_equ', sa.Float(), nullable=True, comment='现金及现金等价物净增加额'),
    sa.Column('c_cash_equ_beg_period', sa.Float(), nullable=True, comment='期初现金及现金等价物余额'),
    sa.Column('c_cash_equ_end_period', sa.Float(), nullable=True, comment='期末现金及现金等价物余额'),
    sa.Column('c_recp_cap_contrib', sa.Float(), nullable=True, comment='吸收投资收到的现金'),
    sa.Column('incl_cash_rec_saims', sa.Float(), nullable=True, comment='其中:子公司吸收少数股东投资收到的现金'),
    sa.Column('uncon_invest_loss', sa.Float(), nullable=True, comment='未确认投资损失'),
    sa.Column('prov_depr_assets', sa.Float(), nullable=True, comment='加:资产减值准备'),
    sa.Column('depr_fa_coga_dpba', sa.Float(), nullable=True, comment='固定资产折旧、油气资产折耗、生产性生物资产折旧'),
    sa.Column('amort_intang_assets', sa.Float(), nullable=True, comment='无形资产摊销'),
    sa.Column('lt_amort_deferred_exp', sa.Float(), nullable=True, comment='长期待摊费用摊销'),
    sa.Column('decr_deferred_exp', sa.Float(), nullable=True, comment='待摊费用减少'),
    sa.Column('incr_acc_exp', sa.Float(), nullable=True, comment='预提费用增加'),
    sa.Column('loss_disp_fiolta', sa.Float(), nullable=True, comment='处置固定、无形资产和其他长期资产的损失'),
    sa.Column('loss_scr_fa', sa.Float(), nullable=True, comment='固定资产报废损失'),
    sa.Column('loss_fv_chg', sa.Float(), nullable=True, comment='公允价值变动损失'),
    sa.Column('invest_loss', sa.Float(), nullable=True, comment='投资损失'),
    sa.Column('decr_def_inc_tax_assets', sa.Float(), nullable=True, comment='递延所得税资产减少'),
    sa.Column('incr_def_inc_tax_liab', sa.Float(), nullable=True, comment='递延所得税负债增加'),
    sa.Column('decr_inventories', sa.Float(), nullable=True, comment='存货的减少'),
    sa.Column('decr_oper_payable', sa.Float(), nullable=True, comment='经营性应收项目的减少'),
    sa.Column('incr_oper_payable', sa.Float(), nullable=True, comment='经营性应付项目的增加'),
    sa.Column('others', sa.Float(), nullable=True, comment='其他'),
    sa.Column('im_net_cashflow_oper_act', sa.Float(), nullable=True, comment='经营活动产生的现金流量净额(间接法)'),
    sa.Column('conv_debt_into_cap', sa.Float(), nullable=True, comment='债务转为资本'),
    sa.Column('conv_copbonds_due_within_1y', sa.Float(), nullable=True, comment='一年内到期的可转换公司债券'),
    sa.Column('fa_fnc_leases', sa.Float(), nullable=True, comment='融资租入固定资产'),
    sa.Column('im_n_incr_cash_equ', sa.Float(), nullable=True, comment='现金及现金等价物净增加额(间接法)'),
    sa.Column('net_dism_capital_add', sa.Float(), nullable=True, comment='拆出资金净增加额'),
    sa.Column('net_cash_rece_sec', sa.Float(), nullable=True, comment='代理买卖证券收到的现金净额(元)'),
    sa.Column('credit_impa_loss', sa.Float(), nullable=True, comment='信用减值损失'),
    sa.Column('use_right_asset_dep', sa.Float(), nullable=True, comment='使用权资产折旧'),
    sa.Column('oth_loss_asset', sa.Float(), nullable=True, comment='其他资产减值损失'),
    sa.Column('end_bal_cash', sa.Float(), nullable=True, comment='现金的期末余额'),
    sa.Column('beg_bal_cash', sa.Float(), nullable=True, comment='减:现金的期初余额'),
    sa.Column('end_bal_cash_equ', sa.Float(), nullable=True, comment='加:现金等价物的期末余额'),
    sa.Column('beg_bal_cash_equ', sa.Float(), nullable=True, comment='减:现金等价物的期初余额'),
    sa.Column('update_flag', sa.Float(), nullable=True, comment='更新标志(1最新）'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('fina_audit',
    sa.Column('id', sa.Integer(), nullable=False, comment='财务审计意见编号'),
    sa.Column('ts_code', sa.String(length=255), nullable=True, comment='TS股票代码'),
    sa.Column('ann_date', sa.String(length=255), nullable=True, comment='公告日期'),
    sa.Column('end_date', sa.String(length=255), nullable=True, comment='报告期'),
    sa.Column('audit_result', sa.String(length=255), nullable=True, comment='审计结果'),
    sa.Column('audit_fees', sa.Float(), nullable=True, comment='审计总费用（元）'),
    sa.Column('audit_agency', sa.String(length=255), nullable=True, comment='会计事务所'),
    sa.Column('audit_sign', sa.String(length=255), nullable=True, comment='签字会计师'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('income_statement',
    sa.Column('id', sa.Integer(), nullable=False, comment='利润表编号'),
    sa.Column('ts_code', sa.String(length=255), nullable=True, comment='TS股票代码'),
    sa.Column('ann_date', sa.String(length=255), nullable=True, comment='公告日期'),
    sa.Column('f_ann_date', sa.String(length=255), nullable=True, comment='实际公告日期'),
    sa.Column('end_date', sa.String(length=255), nullable=True, comment='报告期'),
    sa.Column('report_type', sa.String(length=255), nullable=True, comment='报表类型'),
    sa.Column('comp_type', sa.String(length=255), nullable=True, comment='公司类型'),
    sa.Column('end_type', sa.String(length=255), nullable=True, comment='报告期类型'),
    sa.Column('basic_eps', sa.Float(), nullable=True, comment='基本每股收益'),
    sa.Column('diluted_eps', sa.Float(), nullable=True, comment='稀释每股收益'),
    sa.Column('total_revenue', sa.Float(), nullable=True, comment='营业总收入'),
    sa.Column('revenue', sa.Float(), nullable=True, comment='营业收入'),
    sa.Column('int_income', sa.Float(), nullable=True, comment='利息收入'),
    sa.Column('prem_earned', sa.Float(), nullable=True, comment='已赚保费'),
    sa.Column('comm_income', sa.Float(), nullable=True, comment='手续费及佣金收入'),
    sa.Column('n_commis_income', sa.Float(), nullable=True, comment='手续费及佣金净收入'),
    sa.Column('n_oth_income', sa.Float(), nullable=True, comment='其他经营净收益'),
    sa.Column('n_oth_b_income', sa.Float(), nullable=True, comment='加:其他业务净收益'),
    sa.Column('prem_income', sa.Float(), nullable=True, comment='保险业务收入'),
    sa.Column('out_prem', sa.Float(), nullable=True, comment='减:分出保费'),
    sa.Column('une_prem_reser', sa.Float(), nullable=True, comment='提取未到期责任准备金'),
    sa.Column('reins_income', sa.Float(), nullable=True, comment='其中:分保费收入'),
    sa.Column('n_sec_tb_income', sa.Float(), nullable=True, comment='代理买卖证券业务净收入'),
    sa.Column('n_sec_uw_income', sa.Float(), nullable=True, comment='证券承销业务净收入'),
    sa.Column('n_asset_mg_income', sa.Float(), nullable=True, comment='受托客户资产管理业务净收入'),
    sa.Column('oth_b_income', sa.Float(), nullable=True, comment='其他业务收入'),
    sa.Column('fv_value_chg_gain', sa.Float(), nullable=True, comment='加:公允价值变动净收益'),
    sa.Column('invest_income', sa.Float(), nullable=True, comment='加:投资净收益'),
    sa.Column('ass_invest_income', sa.Float(), nullable=True, comment='其中:对联营企业和合营企业的投资收益'),
    sa.Column('forex_gain', sa.Float(), nullable=True, comment='加:汇兑净收益'),
    sa.Column('total_cogs', sa.Float(), nullable=True, comment='营业总成本'),
    sa.Column('oper_cost', sa.Float(), nullable=True, comment='减:营业成本'),
    sa.Column('int_exp', sa.Float(), nullable=True, comment='减:利息支出'),
    sa.Column('comm_exp', sa.Float(), nullable=True, comment='减:手续费及佣金支出'),
    sa.Column('biz_tax_surchg', sa.Float(), nullable=True, comment='减:营业税金及附加'),
    sa.Column('sell_exp', sa.Float(), nullable=True, comment='减:销售费用'),
    sa.Column('admin_exp', sa.Float(), nullable=True, comment='减:管理费用'),
    sa.Column('fin_exp', sa.Float(), nullable=True, comment='减:财务费用'),
    sa.Column('assets_impair_loss', sa.Float(), nullable=True, comment='减:资产减值损失'),
    sa.Column('prem_refund', sa.Float(), nullable=True, comment='退保金'),
    sa.Column('compens_payout', sa.Float(), nullable=True, comment='赔付总支出'),
    sa.Column('reser_insur_liab', sa.Float(), nullable=True, comment='提取保险责任准备金'),
    sa.Column('div_payt', sa.Float(), nullable=True, comment='保户红利支出'),
    sa.Column('reins_exp', sa.Float(), nullable=True, comment='分保费用'),
    sa.Column('oper_exp', sa.Float(), nullable=True, comment='营业支出'),
    sa.Column('compens_payout_refu', sa.Float(), nullable=True, comment='减:摊回赔付支出'),
    sa.Column('insur_reser_refu', sa.Float(), nullable=True, comment='减:摊回保险责任准备金'),
    sa.Column('reins_cost_refund', sa.Float(), nullable=True, comment='减:摊回分保费用'),
    sa.Column('other_bus_cost', sa.Float(), nullable=True, comment='其他业务成本'),
    sa.Column('operate_profit', sa.Float(), nullable=True, comment='营业利润'),
    sa.Column('non_oper_income', sa.Float(), nullable=True, comment='加:营业外收入'),
    sa.Column('non_oper_exp', sa.Float(), nullable=True, comment='减:营业外支出'),
    sa.Column('nca_disploss', sa.Float(), nullable=True, comment='其中:减:非流动资产处置净损失'),
    sa.Column('total_profit', sa.Float(), nullable=True, comment='利润总额'),
    sa.Column('income_tax', sa.Float(), nullable=True, comment='所得税费用'),
    sa.Column('n_income', sa.Float(), nullable=True, comment='净利润(含少数股东损益)'),
    sa.Column('n_income_attr_p', sa.Float(), nullable=True, comment='净利润(不含少数股东损益)'),
    sa.Column('minority_gain', sa.Float(), nullable=True, comment='少数股东损益'),
    sa.Column('oth_compr_income', sa.Float(), nullable=True, comment='其他综合收益'),
    sa.Column('t_compr_income', sa.Float(), nullable=True, comment='综合收益总额'),
    sa.Column('compr_inc_attr_p', sa.Float(), nullable=True, comment='归属于母公司(或股东)的综合收益总额'),
    sa.Column('compr_inc_attr_m_s', sa.Float(), nullable=True, comment='归属于少数股东的综合收益总额'),
    sa.Column('ebit', sa.Float(), nullable=True, comment='息税前利润'),
    sa.Column('ebitda', sa.Float(), nullable=True, comment='息税折旧摊销前利润'),
    sa.Column('insurance_exp', sa.Float(), nullable=True, comment='保险业务支出'),
    sa.Column('undist_profit', sa.Float(), nullable=True, comment='年初未分配利润'),
    sa.Column('distable_profit', sa.Float(), nullable=True, comment='\t可分配利润'),
    sa.Column('rd_exp', sa.Float(), nullable=True, comment='研发费用'),
    sa.Column('fin_exp_int_exp', sa.Float(), nullable=True, comment='财务费用:利息费用'),
    sa.Column('fin_exp_int_inc', sa.Float(), nullable=True, comment='财务费用:利息收入'),
    sa.Column('transfer_surplus_rese', sa.Float(), nullable=True, comment='盈余公积转入'),
    sa.Column('transfer_housing_imprest', sa.Float(), nullable=True, comment='住房周转金转入'),
    sa.Column('transfer_oth', sa.Float(), nullable=True, comment='其他转入'),
    sa.Column('adj_lossgain', sa.Float(), nullable=True, comment='调整以前年度损益'),
    sa.Column('withdra_legal_surplus', sa.Float(), nullable=True, comment='提取法定盈余公积'),
    sa.Column('withdra_legal_pubfund', sa.Float(), nullable=True, comment='提取法定公益金'),
    sa.Column('withdra_biz_devfund', sa.Float(), nullable=True, comment='提取企业发展基金'),
    sa.Column('withdra_rese_fund', sa.Float(), nullable=True, comment='提取储备基金'),
    sa.Column('withdra_oth_ersu', sa.Float(), nullable=True, comment='提取任意盈余公积金'),
    sa.Column('workers_welfare', sa.Float(), nullable=True, comment='职工奖金福利'),
    sa.Column('distr_profit_shrhder', sa.Float(), nullable=True, comment='可供股东分配的利润'),
    sa.Column('prfshare_payable_dvd', sa.Float(), nullable=True, comment='应付优先股股利'),
    sa.Column('comshare_payable_dvd', sa.Float(), nullable=True, comment='应付普通股股利'),
    sa.Column('capit_comstock_div', sa.Float(), nullable=True, comment='转作股本的普通股股利'),
    sa.Column('net_after_nr_lp_correct', sa.Float(), nullable=True, comment='扣除非经常性损益后的净利润（更正前）'),
    sa.Column('credit_impa_loss', sa.Float(), nullable=True, comment='信用减值损失'),
    sa.Column('net_expo_hedging_benefits', sa.Float(), nullable=True, comment='净敞口套期收益'),
    sa.Column('oth_impair_loss_assets', sa.Float(), nullable=True, comment='其他资产减值损失'),
    sa.Column('total_opcost', sa.Float(), nullable=True, comment='营业总成本（二）'),
    sa.Column('amodcost_fin_assets', sa.Float(), nullable=True, comment='以摊余成本计量的金融资产终止确认收益'),
    sa.Column('oth_income', sa.Float(), nullable=True, comment='其他收益'),
    sa.Column('asset_disp_income', sa.Float(), nullable=True, comment='资产处置收益'),
    sa.Column('continued_net_profit', sa.Float(), nullable=True, comment='持续经营净利润'),
    sa.Column('end_net_profit', sa.Float(), nullable=True, comment='终止经营净利润'),
    sa.Column('update_flag', sa.Float(), nullable=True, comment='\t更新标识'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=15), nullable=False),
    sa.Column('password', sa.String(length=12), nullable=False),
    sa.Column('phone', sa.String(length=11), nullable=True),
    sa.Column('email', sa.String(length=20), nullable=True),
    sa.Column('rdatetime', sa.DateTime(), nullable=True),
    sa.Column('rudatetime', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('phone')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('income_statement')
    op.drop_table('fina_audit')
    op.drop_table('cash_flow')
    op.drop_table('balance_sheet')
    # ### end Alembic commands ###
