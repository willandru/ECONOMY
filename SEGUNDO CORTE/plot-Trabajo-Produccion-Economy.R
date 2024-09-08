
#LEY DE RENDIMIENTOS MARGINALES DECRECIENTES: Ejemplo

L <- c(0:13) # TRABAJO : L
q <- c(0,5,18,36,56,75,90,98,104,108,110,110,108,104) # PRODUCCION: q
plot(L,q)

deltaL <- c(0, diff(L))
deltaL
deltaq <- c(0, diff(q))
deltaq

PM_L <- deltaq / deltaL
PM_L
PM_eL <- q/L
PM_eL

#LA PRODUCCION CON DOS FACTORES VARIABLES 
#En el largo plazo, tanto el capital como el trabajo son variables
#Isocuantas: Curvas que muestran combinaciones eficientes de trabajo y capital
#que producen el mismo nivel de produccion

K <- c(1:6)
K
L <- matrix(c(10, 14, 17, 20, 22, 24,
            14, 20, 24, 28, 32, 35,
            17, 24, 30, 35, 39, 42, 
            20, 28, 35, 40, 45, 49,
            22, 32, 39, 45, 50, 55,
            24, 35, 42, 49, 55, 60), ncol = 6)
L

matplot(L, K, type = "b", pch = 1, col = 1:ncol(L), xlab = "L", ylab = "K", lty = 1)
legend("bottomright", legend = paste("Col", 1:ncol(L)), col = 1:ncol(L), pch = 1, lty = 1)
library(kableExtra)
library(kableExtra)
L_df <- as.data.frame(L)

# Format and display the table
kable(L_df, caption = "Produccion con dos factores Variables", col.names = paste("Column", 1:ncol(L_df))) %>%
  kable_styling(bootstrap_options = c("striped", "hover", "condensed", "responsive"), 
                full_width = F, 
                position = "center")



# Combine K with L_df
combined_df <- cbind(K, L_df)

# Rename the columns (optional)
colnames(combined_df) <- c("K", paste("L", 1:ncol(L_df), sep = ""))
# Format and display the table
kable(combined_df, caption = "Produccion con dos factores Variables", col.names = c("K", paste("L", 1:ncol(L_df), sep = ""))) %>%
  kable_styling(bootstrap_options = c("striped", "hover", "condensed", "responsive"), 
                full_width = F, 
                position = "center")


install.packages("plotly")  # Install if you haven't already
library(plotly)

# Create the 3D plot
plot_ly(x = rep(1:6, each = 6),
        y = rep(1:6, times = 6),
        z = as.vector(L),
        type = 'scatter3d',
        mode = 'markers') %>%
  layout(scene = list(
    xaxis = list(title = "X"),
    yaxis = list(title = "Y"),
    zaxis = list(title = "Z")
  ))
