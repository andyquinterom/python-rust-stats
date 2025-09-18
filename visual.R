library(readr)
library(dplyr)
library(tidyr)
library(ggplot2)
library(lubridate)

read_csv("output/new_projects.csv") |>
  select(-total) |>
  pivot_longer(
    cols = -first_date,
    names_to = "Language",
    values_to = "count"
  ) |>
  mutate(
    first_date = as.Date(first_date),
    year_start = floor_date(first_date, "year")
  ) |>
  group_by(Language, year_start) |>
  summarise(
    yearly_count = sum(count),
    .groups = "drop"
  ) |>
  ggplot(aes(x = year_start, y = yearly_count, color = Language)) +
  geom_line(linewidth = 2) +
  scale_color_manual(
    name = "Language",
    values = c(
      "Rust" = "orange",
      "Cython" = "#1E90FF",
      "C/C++" = "#006400"
    )
  ) +
  labs(
    title = "New Python Packages in PyPi by Language (yearly)",
    x = "Year",
    y = "Number of New Projects",
    color = "Language"
  ) +
  theme_minimal(base_size = 28) +
  theme(
    legend.position = "top",
    plot.title = element_text(hjust = 0.5)
  )