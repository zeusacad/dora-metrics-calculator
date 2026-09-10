"""
Calculadora de Métrica DORA - Tiempo de Ciclo
Simula el cálculo del tiempo promedio entre el inicio y despliegue de tareas.
"""

from datetime import datetime
from typing import List, Dict

class DoraMetricsCalculator:
    """Calcula métricas DORA de tiempo de ciclo."""
    
    def __init__(self):
        self.tasks: List[Dict] = []
    
    def add_task(self, task_id: str, start_date: str, deployment_date: str) -> None:
        """
        Añade una tarea con fecha de inicio y despliegue.
        
        Args:
            task_id: Identificador de la tarea
            start_date: Fecha de inicio (formato: YYYY-MM-DD HH:MM:SS)
            deployment_date: Fecha de despliegue (formato: YYYY-MM-DD HH:MM:SS)
        """
        task = {
            'id': task_id,
            'start_date': datetime.strptime(start_date, "%Y-%m-%d %H:%M:%S"),
            'deployment_date': datetime.strptime(deployment_date, "%Y-%m-%d %H:%M:%S")
        }
        self.tasks.append(task)
    
    def calculate_cycle_time(self, task: Dict) -> float:
        """
        Calcula el tiempo de ciclo en horas para una tarea.
        
        Args:
            task: Diccionario con información de la tarea
            
        Returns:
            Tiempo de ciclo en horas
        """
        time_delta = task['deployment_date'] - task['start_date']
        hours = time_delta.total_seconds() / 3600
        return hours
    
    def get_average_cycle_time(self) -> float:
        """
        Calcula el tiempo de ciclo promedio de todas las tareas.
        
        Returns:
            Tiempo de ciclo promedio en horas
        """
        if not self.tasks:
            return 0.0
        
        total_time = sum(self.calculate_cycle_time(task) for task in self.tasks)
        return total_time / len(self.tasks)
    
    def print_report(self) -> None:
        """Imprime un reporte detallado de las métricas DORA."""
        print("\n" + "="*70)
        print("REPORTE DE MÉTRICAS DORA - TIEMPO DE CICLO")
        print("="*70 + "\n")
        
        for task in self.tasks:
            cycle_time = self.calculate_cycle_time(task)
            print(f"Tarea: {task['id']}")
            print(f"  Inicio:     {task['start_date'].strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"  Despliegue: {task['deployment_date'].strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"  Tiempo de ciclo: {cycle_time:.2f} horas ({cycle_time/24:.2f} días)")
            print()
        
        avg_cycle_time = self.get_average_cycle_time()
        print("-"*70)
        print(f"TIEMPO DE CICLO PROMEDIO: {avg_cycle_time:.2f} horas ({avg_cycle_time/24:.2f} días)")
        print("="*70 + "\n")


def main():
    """Función principal - Simula el cálculo de métrica DORA."""
    
    # Crear instancia del calculador
    calculator = DoraMetricsCalculator()
    
    # Añadir tres tareas con fechas de inicio y despliegue
    calculator.add_task(
        task_id="TASK-001",
        start_date="2026-09-01 08:00:00",
        deployment_date="2026-09-03 14:30:00"
    )
    
    calculator.add_task(
        task_id="TASK-002",
        start_date="2026-09-04 09:15:00",
        deployment_date="2026-09-06 16:45:00"
    )
    
    calculator.add_task(
        task_id="TASK-003",
        start_date="2026-09-07 10:00:00",
        deployment_date="2026-09-09 11:20:00"
    )
    
    # Mostrar el reporte
    calculator.print_report()


if __name__ == "__main__":
    main()
