# coding=utf-8
from openerp import models, fields, api

class setting_aid_system(models.Model):
    _name = 'setting.aid.system'

    summons = fields.Selection(
        [('day','月日流水號'),('month','月流水號'),('year','流水號'),('free','自行輸入')
         ,('threenumday','前三碼+月日流水號'),('threemonth','前三碼+月流水號')],string='傳票號碼')
    buysell = fields.Selection(
        [('day','月日流水號'),('month','月流水號'),('year','流水號'),('free','自行輸入')
         ,('threenumday','前三碼+月日流水號'),('threemonth','前三碼+月流水號')],string='進銷單號')
    consumables = fields.Selection(
        [('day','月日流水號'),('month','月流水號'),('year','流水號'),('free','自行輸入')
         ,('threenumday','前三碼+月日流水號'),('threemonth','前三碼+月流水號')],string='耗材單號')
    openaccount = fields.Selection(
        [('day','月日流水號'),('month','月流水號'),('year','流水號'),('free','自行輸入')
         ,('threenumday','前三碼+月日流水號'),('threemonth','前三碼+月流水號')],string='立沖單號')
    summonsname = fields.Char('傳票單代號')
    buysellname = fields.Char('進銷單代號')
    consumablesname = fields.Char('耗材單代號')
    openaccountname = fields.Char('立沖單代號')
    classinform = fields.Boolean('單號含單別')
    address = fields.Boolean('地址快速輸入')
    aummonsasbuysell = fields.Boolean('進銷單號同傳票號碼')
    yearinform = fields.Boolean('單號含年度')
    defaultaddress = fields.Char('開窗縣市初值')
