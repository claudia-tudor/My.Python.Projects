#2

import pandas as pd_tci 
import os
import tkinter.filedialog as fd_tci

current_directory_tci = os.getcwd()

products_tci = [ "Meshforce Mesh WiFi System M3s Suite - Up to 6,000 sq. ft. Whole Home", 
                "True Wireless Earbuds, Bluetooth 5.0 Headphone, in-Ear Button Control Hi-Fi", 
                "Seducte 4 Pack Leather Airtag Case for Apple AirTag, Protective Leather Airtags", 
                "Save on SteelSeries Aerox 5 Wireless - Lightweight Wireless Gaming Mouse", 
                "Webcam Cover Slide 6 Pack, 0.027 inch Ultra-Thin Metal Magnet Web Camera", 
                "Wireless Earbuds Bluetooth 5.0 Mini Headphones, Hi-Fi Stereo in-Ear",
                "Tapela E7 Wireless Active Noise Cancelling Headphones", 
                "Wireless Earbuds Bluetooth 5.0 Headphones HiFi Stereo Noise Cancelling with Wireless"
                , "Latest Upgrade Bluetooth 5.0 True Wireless Earbuds with Charging Case Waterproof", 
                "True Wireless Earbuds, Bluetooth Earbuds 30Hrs Cycle Playtime with Charging Case" ]

prices_tci = [118.99, 26.99, 12.99, 12.56, 9.34, 25.99, 49.99, 30.59, 19.99, 19.99]

df_accessories_tci = pd_tci.DataFrame({"Accessories name": products_tci, "Price": prices_tci})

accessories_path_tci = current_directory_tci + "/Accessories2.xlsx" 
df_accessories_tci.to_excel(accessories_path_tci, sheet_name="Amazon", engine="xlsxwriter")

books_path_tci = fd_tci.askopenfilename(title="Select Books.xlsx", 
                                        filetypes=[("Excel files", "*.xlsx")])

df_books_tci = pd_tci.read_excel(books_path_tci, sheet_name=0, usecols='A:C,H', header=0, nrows=60)

books_filtered_path_tci = current_directory_tci + "/books_filtered_tci2.xlsx" 
df_books_tci.to_excel(books_filtered_path_tci, sheet_name="Filtered Books", engine="xlsxwriter")
