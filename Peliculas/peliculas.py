
# -*- coding: utf-8 -*-

from openerp.osv import fields, osv , orm
from datetime import time, datetime
from openerp.tools.translate import _


class peliculas_modelo(osv.osv):
	_name = 'peliculas.modelo'
	_description = 'Formulario de Peliculas'
	_columns = {
	     # Campo oblidatorio para buscar , readonly = True
	     'name' : fields.char('Nombre' , size=256, required=True, help='Este es el nombre'),
		 'categoria' : fields.char('Categoria' , size=256, required=True, help='Esto es la categoria de la pelicula'),
		 'duracion' : fields.char('Duracion' , size=256, required=True, help='Duracion de la pelicula'),
		 'anotacion' : fields.char('Anotacion' , size=300, required=True, help='Introduce cualquier anotacion sobre la pelicula'),
		'fecha': fields.date('Fecha Estreno', required=True ),
       'active': fields.boolean('Activo'),
	}
	_defaults = {
       'active' : 'true',
	}


peliculas_modelo()
