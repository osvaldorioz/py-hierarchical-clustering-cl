El **Hierarchical Clustering** es un método de agrupamiento que construye una jerarquía de clusters. Se puede realizar de diferentes maneras dependiendo de cómo se mide la distancia entre los clusters.  

### **Diferencias entre Single Linkage y Complete Linkage**  

| Criterio           | **Single Linkage** | **Complete Linkage** |
|--------------------|------------------|------------------|
| **Definición**     | La distancia entre dos clusters es la menor distancia entre cualquier par de puntos (uno de cada cluster). | La distancia entre dos clusters es la mayor distancia entre cualquier par de puntos (uno de cada cluster). |
| **Tendencia en la agrupación** | Tiende a formar **clusters encadenados** o alargados. | Tiende a formar **clusters compactos y bien separados**. |
| **Sensibilidad al ruido** | Sensible al **efecto "chaining"**, donde puntos dispersos pueden conectar clusters grandes. | Menos sensible al chaining, pero puede generar clusters de tamaño desigual. |
| **Casos de uso**  | Bueno cuando los datos forman estructuras en forma de cadena. | Mejor cuando los clusters son más esféricos y bien definidos. |

En resumen, **Single Linkage** es útil para detectar estructuras en forma de cadena, mientras que **Complete Linkage** genera clusters más compactos y bien separados.
