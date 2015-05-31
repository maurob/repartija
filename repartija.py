# -- coding=utf-8 --

class Repartija:
    """ Permite definir los precios individuales por hora de cada persona que trabaja 
    y calcular las ganancias individuales, exponiendo un único precio por hora para
    quien se trabaja. """

    def set_precios_por_hora(self, precios_por_hora):
        """ El *precio_por_hora* es un diccionario tipo `{'mauro':170, 'martin':230}` """
        self.precios_por_hora = {individuo: float(precio) for individuo, precio in precios_por_hora.items()}

    def set_trabajo(self, horas):
        """ Define la cantidad de horas trabajadas por cada individuo en el diccionario *horas* """
        self.horas_trabajadas = {individuo: float(precio) for individuo, precio in horas.items()}
        
    def individuos(self):
        """ Devuelve la lista de individuos """
        return self.precios_por_hora.keys()

    def precio_medio_por_hora(self):
        """ Es el precio que se va a cobrar por hora trabajada """
        return sum(self.precios_por_hora.values()) / len(self.precios_por_hora)

    def ganancia_individual(self):
        """ Es el valor que se lleva aca individuo """
        try:
            ajuste = self.precio_real() / self.precio_deceado()
        except ZeroDivisionError: # Porque los único que trabajaron trabajan grátis
            d = {None: self.precio_real()}
            d.update({individuo: 0.0 for individuo in self.individuos()})
            return d
        
        return {individuo: self.horas_trabajadas[individuo] * precio_por_hora * ajuste
                for individuo, precio_por_hora in self.precios_por_hora.items()}
        
    def precios_por_hora_ajustado(self):
        """ Es el precio por hora individual correjido, que depende de las horas trabajadas """
        ajuste = self.ajuste()
        return {individuo: precio_por_hora * ajuste
                for individuo, precio_por_hora in self.precios_por_hora.items()}

    def ajuste(self):
        """ Coeficiente de ajuste para alcanzar el precio real a partir del precio deceado """
        return self.precio_real() / self.precio_deceado()

    def total_de_horas_trabajadas(self):
        """ Es la suma de las horas trabajas de cada uno """
        return sum(self.horas_trabajadas.values())
        
    def precio_real(self):
        """ Es el precio que se va a cobrar """
        return float(self.precio_medio_por_hora() * self.total_de_horas_trabajadas())
    
    def precio_deseado(self):
        """ Es el precio que se pretende cobrar en función del precio horario de cada uno """
        return float(sum(self.horas_trabajadas[individuo] * precio_por_hora
                   for individuo, precio_por_hora in self.precios_por_hora.items()))
 
