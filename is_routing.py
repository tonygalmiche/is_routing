# -*- coding: utf-8 -*-

from openerp.osv import osv, fields

#Permet de faire les traductions avec la fonction _()
from openerp.tools.translate import _


class mrp_routing_workcenter(osv.osv):
    _name = 'mrp.routing.workcenter'
    _inherit = 'mrp.routing.workcenter'
    
    
    def _calcul_hour_nbr(self, cr, uid, ids, field_name, arg, context={}):
        result = {}
        for id in ids:
            myself = self.browse(cr, uid, id, context=context)
            res = 0.0
            if myself:
                res = myself.seconds_nbr/float(3600)
                #res = 0.123456
                result[id] = res

        return result
    
    
    
    _columns = {
        'seconds_nbr': fields.float("Nombre de secondes", digits=(12,2), required=False, help="Nombre de secondes"),
        'hour_nbr':    fields.function( _calcul_hour_nbr, digits=(12,6), method=True, type='float', string='Champ calculé', store=True, readonly=True)
        
    }
    
#        'hour_nbr':    fields.float("Nombre d'heures"   , digits=(12,6), required=False, help="Nombre d'heures"),
    
#        'hour_nbr': fields.float('Number of Hours', digits=(12,6), required=True, help="Time in hours for this Work Center to achieve the operation of the specified routing."),
    
    
    #def seconds_nbr_change(self, cr, uid, ids, seconds, context=None):  
        #result = {}
        #for id in ids:
            #myself = self.browse(cr, uid, id, context=context)
            #res = 0
            #if myself:
                #hour_nbr = seconds/3600.000000
        #return {
            #'value': {
                #'hour_nbr': seconds/3600.000000
            #}
        #}    
  
    #def hour_nbr_change(self, cr, uid, ids, hour, context=None):  
        #result = {}
        #for id in ids:
            #myself = self.browse(cr, uid, id, context=context)
            #res = 0
            #if myself:
                #seconds_nbr = round(hour*3600,2)
        #return {
            #'value': {
                #'seconds_nbr': hour+0.01
            #}
        #}    
  
  
mrp_routing_workcenter()


