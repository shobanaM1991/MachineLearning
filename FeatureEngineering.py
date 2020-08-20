from matplotlib.colors import LinearSegmentedColormap
import numpy as np
from dateutil import parser
from datetime import datetime
import tkinter as tkinter
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import pandas as pd
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle, Paragraph
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, inch, A3
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.graphics import renderPDF
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.barcharts import VerticalBarChart

import os
global str
gbl = globals()


class WindowApp(Tk):

    def __init__(self):
        super(WindowApp, self).__init__()
        self.title("Report")
        self.minsize(480, 200)
        self.configure(background='#4D4D4D')
        self.emptylist_label = []
        self.emptylist_button = []
        self.emptylist_path = []
        self.inputlist_label = []
        self.entrylist_label = []
        self.inputlist_label1 = []
        self.entrylist_label1 = []
        self.inputlist_label2 = []
        self.entrylist_label2 = []

        for i in range(1):
            self.emptylist_label.append(
                Label(self, text="Open File No" + str(i+1)))
            # self.emptylist[i] = ttk.LabelFrame(self, text="Open File No" + str(i+1))
            # self.append(i)
            self.emptylist_label[i].grid(row=i, column=0)
            self.emptylist_button.append(
                Button(self, text="Select CSV file" + str(i+1), command=self.csv))
            self.emptylist_button[i].grid(row=i, column=1)
            # self.emptylist_path.append(
            #     Button(self, text="Select excel file" + str(i+1), command=self.fileDialog))
            # self.emptylist_path[i].grid(row=i, column=2)

        for i in range(1):
            self.number_var = tkinter.StringVar()
            self.inputlist_label.append(Label(self, text="Delay Time"))
            self.inputlist_label[i].grid(row=3, column=0, pady=(5, 5))
            self.entrylist_label.append(
                Entry(self, textvariable=self.number_var))
            self.entrylist_label[i].grid(row=3, column=1)

        for i in range(1):
            self.number_var1 = tkinter.StringVar()
            self.inputlist_label1.append(Label(self, text="No. of Sensors"))
            self.inputlist_label1[i].grid(row=4, column=0, pady=(5, 5))
            self.entrylist_label1.append(
                Entry(self, textvariable=self.number_var1))
            self.entrylist_label1[i].grid(row=4, column=1)

        for i in range(1):
            self.number_var2 = tkinter.StringVar()
            self.inputlist_label2.append(
                Label(self, text="1st Test sensor address"))
            self.inputlist_label2[i].grid(row=5, column=0, pady=(5, 5))
            self.entrylist_label2.append(
                Entry(self, textvariable=self.number_var2))
            self.entrylist_label2[i].grid(row=5, column=1)

        self.button()

    def button(self):
        # self.button = ttk.Button(self.labelFrame, text="Browse File No 1", command=self.fileDialog)
        self.button = ttk.Button(
            self, text="PDF", command=self.Pdf)
        self.button.grid(row=13, column=0, pady=(5, 5))
        # self.button = ttk.Button(
        #     self, text="Plot-middle-4-sensors", command=self.plt_sensors5to8)
        # self.button.grid(row=13, column=1, pady=(5, 5))
        # self.button = ttk.Button(
        #     self, text="Plot-last-2-sensors", command=self.plt_last2sensors)
        # self.button.grid(row=13, column=2, pady=(5, 5), padx=5)
        self.button = ttk.Button(self, text="Compare",
                                 command=self.static_criteria)
        self.button.grid(row=5, column=2)
        self.button = ttk.Button(self, text="Close", command=self.quit)
        self.button.grid(row=13, column=1, pady=(5, 5))

    def csv(self):
        self.filename = filedialog.askopenfilename()
        self.v = tkinter.StringVar()
        self.v.set(self.filename)
        self.Cov = pd.read_csv(
            self.filename, delimiter=';', encoding='latin-1', low_memory=False)
        self.Cov = self.Cov.fillna('')
        self.Cov.columns = self.Cov.columns+'_'+self.Cov.iloc[1, :]
        self.Cov.iloc[6:, ]
        self.Cov.drop(index=[0, 1, 2, 3, 4, 5], inplace=True)
        self.Cov.rename(columns={'Gerät_Kommentar': 'Date'}, inplace=True)
        self.Cov.rename(columns={'Unnamed: 1_': 'Time'}, inplace=True)
        self.Cov1 = self.Cov[['Date', 'Time']]
        self.Cov2 = self.Cov.drop(['Date', 'Time'], axis=1)
        self.Cov2.columns = self.Cov2.columns.str.strip()
        self.Cov2 = self.Cov2.stack().str.replace(',','.').unstack()
        self.Cov2 = self.Cov2.apply(pd.to_numeric, errors='coerce')
        #self.Cov2 = (self.Cov2.str.replace(',', '.'))
        #self.Cov2 = pd.concat([self.Cov2[col].str.split().str[0].str.replace(',', '.').astype(float) for col in self.Cov2], axis=1)
        #self.Cov2 = pd.concat([self.Cov2[col].apply(str).str.replace(',', '.').astype(float) for col in self.Cov2], axis=1)
        # for i in range(len( self.Cov2.columns)):
        #     self.Cov2.iloc[:, i] = self.Cov2.iloc[:, i].astype(float)
        print(self.Cov2.dtypes)
        self.df = pd.concat([self.Cov1, self.Cov2], axis=1, sort=False)

        # self.Cov1.stack().str.replace(',','.').unstack()
        # print('After delete an index: ', self.Cov.head(10))
        self.df.columns = self.df.columns.str.strip()
        #self.df['Time'] = self.df['Time'].astype(str)
        #self.df["Time"] = self.df["Time"].str.replace(":", "", regex=True)
    def static_criteria(self):
        print(self.df.iloc[:, 2])
        # for i in range(len(self.df)-1):
        # self.df.loc[index, 'Formula_static_sen1'] =  abs(self.df.loc[index, '0_p_ÖL    In']-self.df.loc[index, '1_Wika R1 0-50'])  !!!!wrong calculation
        self.df['Formula_static_Ref_sen'] = abs(self.df.iloc[:, 2].diff(periods=-1))

        print(self.df.iloc[:, int(self.entrylist_label2[0].get())])
        for i in range(int(self.entrylist_label1[0].get())):
            self.df['Delta_P' + str(i+1)] = abs(self.df.iloc[:,
                                                             2] - self.df.iloc[:, i+int(self.entrylist_label2[0].get())])

        #self.df['neg_2_per_FS'] = self.df.iloc[:, 2] - (50*(0.02))
        self.df['Pos_2_per_FS'] = (30*(0.02))
        #self.df['neg_5_per_FS'] = self.df.iloc[:, 2] - (50*(0.05))
        self.df['Pos_5_per_FS'] = (30*(0.05))
        #self.df['neg_10_per_FS'] = self.df.iloc[:, 2] - (50*(0.1))
        self.df['Pos_10_per_FS'] = (30*(0.1))
        #self.df['neg_15_per_FS'] = self.df.iloc[:, 2] - (50*(0.15))
        self.df['Pos_15_per_FS'] = (30*(0.15))
        self.static_Ast = []
        self.static_Bst = []
        self.static_Cst = []
        self.static_Dst = []
        self.static_A_to_Bst = []
        self.static_B_to_Cst = []
        self.dynamic_A = []
        self.dynamic_B = []
        self.dynamic_C = []
        self.dynamic_D = []
        self.count_st_sen = []
        self.count_dy_sen = []
        self.df.loc[self.df['Formula_static_Ref_sen'] <= 1, 'St_or_Dy'] = 1
        self.df.loc[self.df['Formula_static_Ref_sen'] > 1, 'St_or_Dy'] = 0
        self.count_st_sen.append(self.df['St_or_Dy'].sum())
        self.count_dy_sen.append(len(self.df)-  self.count_st_sen[0])
        self.df = self.df.reset_index(drop=True)
        self.df.dropna(subset=['St_or_Dy'], inplace=True)
        self.df = self.df.reset_index(drop=True)
        print(self.df.head())
        if (self.df[self.df.St_or_Dy == 1].iloc[0].any()):
            for i in range(10):
                self.df.loc[i, 'results'] = 'delete'
        elif (self.df[self.df.St_or_Dy == 0].iloc[0].any()):
            self.df[0, 'results'] = 'keep'
        else:
            self.df[0, 'results'] = 'think'

        conditions = [(self.df['St_or_Dy'] > self.df['St_or_Dy'].shift(1)), (self.df['St_or_Dy'] < self.df['St_or_Dy'].shift(1))]
        choices = ['static', 'dynamic']
        self.df['statte'] = np.select(conditions, choices, default='remain')
        print(len(self.df.statte == 'static'))
        index_list = self.df.statte[self.df.statte == 'static'].index.tolist()
        print(len(index_list))
        #print(index_list)
        index_list_updated = []
        finallist = []
        #index_list_updated = [elem+i for i in range(11) for elem in index_list]
        for i in index_list:
            for j in range(10):
                index_list_updated.append(i+j)

        print(len(index_list_updated))
        #print(index_list_updated)
        finallist = np.unique(index_list_updated) 
        #print(finallist)
        print(len(finallist))
        # for n in range(1, len(index_list)):
        #     if ((index_list[n])-(index_list[n-1]) <= 2):
        #         index_list_updated.append(index_list[n])

        # finallist = [ele for ele in index_list if ele not in index_list_updated] 
        #print(len(index_list_updated))
        #print(index_list_updated)
        #print(len(finallist))
        #print(finallist)
        self.df.loc[:,'static_list'] = pd.Series(index_list)
        self.df.loc[:,'static_list_incre'] = pd.Series(finallist)
        print(self.df.head(1))
        self.df = self.df.drop(finallist)
        # for value in self.df.static_list_incre:
        #     if value <= (len(self.df)-10):
        #         print([value])
        #         self.df = self.df.drop([value])
                    #self.df3 = self.df.loc[[value+j], :]
                    #self.df.loc[value+j, 'static_list_del'] = 'delete'

        self.df = self.df.drop(self.df[(self.df['results'] == 'delete')].index)
        #self.df = self.df.drop(self.df[(self.df['static_list_del'] == 'delete')].index)
        #self.df.to_excel('staticres1.xlsx', index=0, header=True)
        #self.df = self.df.drop(['static_list_del'], axis=1)
        self.df = self.df.reset_index(drop=True)
        self.df_filtered = self.df.copy()
        #print(self.df_filtered.head())          
        self.df1 = self.df[self.df_filtered['St_or_Dy'] == 1].copy()
        self.df2 = self.df[self.df_filtered['St_or_Dy'] == 0].copy()
        #self.df2.to_excel('staticres.xlsx', index=0, header=True)
        print(self.df.head())  
        print(len(self.df1))  
        print(len(self.df2))

        for i in range(int(self.entrylist_label1[0].get())): 
            self.df1['Delta_PAst' + str(i+1)] = self.df1['Delta_P' + str(i+1)] <= self.df1['Pos_2_per_FS']
            self.df1['Delta_PBst' + str(i+1)] = np.logical_and(self.df1['Delta_P' + str(i+1)] > self.df1['Pos_2_per_FS'], self.df1['Delta_P' + str(i+1)] <= self.df1['Pos_5_per_FS'])
            self.df1['Delta_PCst' + str(i+1)] = np.logical_and(self.df1['Delta_P' + str(i+1)] > self.df1['Pos_5_per_FS'], self.df1['Delta_P' + str(i+1)] <= self.df1['Pos_10_per_FS'])
            self.df1['Delta_PDst' + str(i+1)] = self.df1['Delta_P' + str(i+1)] > self.df1['Pos_10_per_FS']
            self.static_Ast.append(self.df1['Delta_PAst' + str(i+1)].sum())
            self.static_Bst.append(self.df1['Delta_PBst' + str(i+1)].sum())
            self.static_Cst.append(self.df1['Delta_PCst' + str(i+1)].sum())
            self.static_Dst.append(self.df1['Delta_PDst' + str(i+1)].sum())
    
        for i in range(int(self.entrylist_label1[0].get())):
            self.df2['Delta_PA_Dy' + str(i+1)] = self.df2['Delta_P' + str(i+1)] <= self.df2['Pos_5_per_FS']
            self.df2['Delta_PB_Dy' + str(i+1)] = np.logical_and(self.df2['Delta_P' + str(
                i+1)] > self.df2['Pos_5_per_FS'], self.df2['Delta_P' + str(i+1)] <= self.df2['Pos_10_per_FS'])
            self.df2['Delta_PC_Dy' + str(i+1)] = np.logical_and(self.df2['Delta_P' + str(
                i+1)] > self.df2['Pos_10_per_FS'], self.df2['Delta_P' + str(i+1)] <= self.df2['Pos_15_per_FS'])
            self.df2['Delta_PD_Dy' + str(i+1)] = self.df2['Delta_P' + str(i+1)] > self.df2['Pos_15_per_FS']
            self.dynamic_A.append(self.df2['Delta_PA_Dy' + str(i+1)].sum())
            self.dynamic_B.append(self.df2['Delta_PB_Dy' + str(i+1)].sum()) 
            self.dynamic_C.append(self.df2['Delta_PC_Dy' + str(i+1)].sum())
            self.dynamic_D.append(self.df2['Delta_PD_Dy' + str(i+1)].sum())

        print("Completed")    
        print(self.static_Ast)
        print(self.static_Bst)
        print(self.static_Cst)
        print(self.static_Dst)
        print(self.dynamic_A)
        print(self.dynamic_B)
        print(self.dynamic_C)
        print(self.dynamic_D)

        #self.df_filtered = pd.concat([self.df1, self.df2], sort=True)
        #self.df_filtered = self.df_filtered.reset_index(drop=True)
        #self.df1.to_excel('static.xlsx', index=0, header=True)
        #self.df2.to_excel('dynamic.xlsx', index=0, header=True)
        #self.df1.to_excel('dynamicres.xlsx', index=0, header=True)
        #self.2.to_csv('results.csv', header=True)

    def Pdf(self):
        c = canvas.Canvas("Report.pdf", pagesize=A4)
        c1 = canvas.Canvas("Report_withoutD.pdf", pagesize=A4)
        # c.translate(inch,inch)
        #c.drawString(30, 750, "A Complete Summay of Test Results")
        path, file_name = os.path.split(self.filename)
        # print(path)
        # print(file_name)

        textobject = c.beginText(30, 800)
        textobject = c1.beginText(30, 800)
        lines = ["A Complete Summay of Test Results",
                 "Filename: " + str(file_name), "Delaytime = 10"]
        for line in lines:
            textobject.textLine(line)

        c.drawText(textobject)
        c1.drawText(textobject)

        styles = getSampleStyleSheet()
        style = styles["BodyText"]
        d00 = self.df.columns[2]
        d0 = self.df.columns[int(self.entrylist_label2[0].get())]
        d1 = self.df.columns[(int(self.entrylist_label2[0].get())+1)]
        d2 = self.df.columns[(int(self.entrylist_label2[0].get())+2)]
        d3 = self.df.columns[(int(self.entrylist_label2[0].get())+3)]
        d4 = self.df.columns[(int(self.entrylist_label2[0].get())+4)]
        d5 = self.df.columns[(int(self.entrylist_label2[0].get())+5)]
        d6 = self.df.columns[(int(self.entrylist_label2[0].get())+6)]
        d7 = self.df.columns[(int(self.entrylist_label2[0].get())+7)]
        d8 = self.df.columns[(int(self.entrylist_label2[0].get())+8)]
        d9 = self.df.columns[(int(self.entrylist_label2[0].get())+9)]
        count_st_sen1 = []
        count_Dy_sen2 = []
        for i in range(int(self.entrylist_label1[0].get())):
            count_st_sen1.append(
                self.static_Ast[i] + self.static_Bst[i] + self.static_Cst[i] + self.static_Dst[i])

        for i in range(int(self.entrylist_label1[0].get())):
            count_Dy_sen2.append(
                self.dynamic_A[i] + self.dynamic_B[i] + self.dynamic_C[i] + self.dynamic_D[i])

        header = Paragraph(
            "<bold><font size=14>Test_Sensors Report</font></bold>", style)

        data = [['S.NO', 'Sensors', 'Static\n(dp.ref\n≤1bar)', 'Dynami\nc(dp.ref\n>1bar)', 'Static\n_A', 'Static\n_B', 'Static\n_C', 'Static\n_D', 'Dyna\nmic_A', 'Dyna\nmic_B', 'Dyna\nmic_C', 'Dyna\nmic_D'],
                ['1', d00, self.count_st_sen[0], self.count_dy_sen[0], '(A_st≤\n2%FS)', '(B_st>2\n%FS&≤5\n%FS)',
                    '(C_st\n>5%FS\n&≤10\n%FS)', '(D_st>\n10%FS)', '(Dy_A\n≤5%FS)', '(Dy_B\n>5%FS\n&≤10%\nFS)', '(Dy_C>\n10%FS&\n≤15%\nFS)', '(Dy_D\n>15\n%FS)'],
                ['2', d0, count_st_sen1[0], count_Dy_sen2[0], self.static_Ast[0], self.static_Bst[0],
                    self.static_Cst[0], self.static_Dst[0], self.dynamic_A[0], self.dynamic_B[0], self.dynamic_C[0], self.dynamic_D[0]],
                ['3', d1, count_st_sen1[1], count_Dy_sen2[1], self.static_Ast[1], self.static_Bst[1],
                    self.static_Cst[1], self.static_Dst[1], self.dynamic_A[1], self.dynamic_B[1], self.dynamic_C[1], self.dynamic_D[1]],
                ['4', d2, count_st_sen1[2], count_Dy_sen2[2], self.static_Ast[2], self.static_Bst[2],
                    self.static_Cst[2], self.static_Dst[2], self.dynamic_A[2], self.dynamic_B[2], self.dynamic_C[2], self.dynamic_D[2]],
                ['5', d3, count_st_sen1[3], count_Dy_sen2[3], self.static_Ast[3], self.static_Bst[3],
                    self.static_Cst[3], self.static_Dst[3], self.dynamic_A[3], self.dynamic_B[3], self.dynamic_C[3], self.dynamic_D[3]],
                ['6', d4, count_st_sen1[4], count_Dy_sen2[4], self.static_Ast[4], self.static_Bst[4],
                    self.static_Cst[4], self.static_Dst[4], self.dynamic_A[4], self.dynamic_B[4], self.dynamic_C[4], self.dynamic_D[4]],
                ['7', d5, count_st_sen1[5], count_Dy_sen2[5], self.static_Ast[5], self.static_Bst[5],
                    self.static_Cst[5], self.static_Dst[5], self.dynamic_A[5], self.dynamic_B[5], self.dynamic_C[5], self.dynamic_D[5]],
                ['8', d6, count_st_sen1[6], count_Dy_sen2[6], self.static_Ast[6], self.static_Bst[6],
                    self.static_Cst[6], self.static_Dst[6], self.dynamic_A[6], self.dynamic_B[6], self.dynamic_C[6], self.dynamic_D[6]],
                ['9', d7, count_st_sen1[7], count_Dy_sen2[7], self.static_Ast[7], self.static_Bst[7],
                    self.static_Cst[7], self.static_Dst[7], self.dynamic_A[7], self.dynamic_B[7], self.dynamic_C[7], self.dynamic_D[7]],
                ['10', d8, count_st_sen1[8], count_Dy_sen2[8], self.static_Ast[8], self.static_Bst[8],
                    self.static_Cst[8], self.static_Dst[8], self.dynamic_A[8], self.dynamic_B[8], self.dynamic_C[8], self.dynamic_D[8]],
                ['11', d9, count_st_sen1[9], count_Dy_sen2[9], self.static_Ast[9], self.static_Bst[9],
                    self.static_Cst[9], self.static_Dst[9], self.dynamic_A[9], self.dynamic_B[9], self.dynamic_C[9], self.dynamic_D[9]]]

        f = Table(data, colWidths=(0.4*inch, 1.2*inch, 0.6*inch, 0.6*inch, 0.6*inch,
                                   0.6*inch, 0.6*inch, 0.6*inch, 0.6*inch, 0.6*inch, 0.6*inch, 0.5*inch), rowHeights=(12*[0.8*inch]))
        #f = Table(data, colWidths=(0.4*inch, 1.2*inch, 0.6*inch, 0.6*inch, 0.6*inch, 0.6*inch, 0.6*inch, 0.6*inch, 0.6*inch, 0.6*inch), rowHeights=(12*[0.8*inch]))
        f.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.25, colors.black),
                               ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                               ('FONTNAME', (0, 0), (-1, -1), 'Courier'),
                               ('FONTSIZE', (0, 0), (-1, -1), 8)]))

        #without condition D for both static and dynamic
        data_withoutD = [['S.NO', 'Sensors', 'Static\n(dp.ref\n≤1bar)', 'Dynami\nc(dp.ref\n>1bar)', 'Static\n_A', 'Static\n_B', 'Static\n_C', 'Dyna\nmic_A', 'Dyna\nmic_B', 'Dyna\nmic_C'],
                ['1', d00, self.count_st_sen[0], self.count_dy_sen[0], '(A_st≤\n2%FS)', '(B_st>2\n%FS&≤5\n%FS)',
                    '(C_st\n>5%FS\n&≤10\n%FS)', '(Dy_A\n≤5%FS)', '(Dy_B\n>5%FS\n&≤10%\nFS)', '(Dy_C>\n10%FS&\n≤15%\nFS)'],
                ['2', d0, count_st_sen1[0], count_Dy_sen2[0], self.static_Ast[0], self.static_Bst[0],
                    self.static_Cst[0], self.dynamic_A[0], self.dynamic_B[0], self.dynamic_C[0]],
                ['3', d1, count_st_sen1[1], count_Dy_sen2[1], self.static_Ast[1], self.static_Bst[1],
                    self.static_Cst[1], self.dynamic_A[1], self.dynamic_B[1], self.dynamic_C[1]],
                ['4', d2, count_st_sen1[2], count_Dy_sen2[2], self.static_Ast[2], self.static_Bst[2],
                    self.static_Cst[2], self.dynamic_A[2], self.dynamic_B[2], self.dynamic_C[2]],
                ['5', d3, count_st_sen1[3], count_Dy_sen2[3], self.static_Ast[3], self.static_Bst[3],
                    self.static_Cst[3], self.dynamic_A[3], self.dynamic_B[3], self.dynamic_C[3]],
                ['6', d4, count_st_sen1[4], count_Dy_sen2[4], self.static_Ast[4], self.static_Bst[4],
                    self.static_Cst[4], self.dynamic_A[4], self.dynamic_B[4], self.dynamic_C[4]],
                ['7', d5, count_st_sen1[5], count_Dy_sen2[5], self.static_Ast[5], self.static_Bst[5],
                    self.static_Cst[5], self.dynamic_A[5], self.dynamic_B[5], self.dynamic_C[5]],
                ['8', d6, count_st_sen1[6], count_Dy_sen2[6], self.static_Ast[6], self.static_Bst[6],
                    self.static_Cst[6], self.dynamic_A[6], self.dynamic_B[6], self.dynamic_C[6]],
                ['9', d7, count_st_sen1[7], count_Dy_sen2[7], self.static_Ast[7], self.static_Bst[7],
                    self.static_Cst[7], self.dynamic_A[7], self.dynamic_B[7], self.dynamic_C[7]],
                ['10', d8, count_st_sen1[8], count_Dy_sen2[8], self.static_Ast[8], self.static_Bst[8],
                    self.static_Cst[8], self.dynamic_A[8], self.dynamic_B[8], self.dynamic_C[8]],
                ['11', d9, count_st_sen1[9], count_Dy_sen2[9], self.static_Ast[9], self.static_Bst[9],
                    self.static_Cst[9], self.dynamic_A[9], self.dynamic_B[9], self.dynamic_C[9]]]

        f_data_withoutD = Table(data_withoutD, colWidths=(0.4*inch, 1.2*inch, 0.6*inch, 0.6*inch, 0.6*inch, 0.6*inch, 0.6*inch, 0.6*inch, 0.6*inch, 0.6*inch), rowHeights=(12*[0.8*inch]))
        f_data_withoutD.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.25, colors.black),
                               ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                               ('FONTNAME', (0, 0), (-1, -1), 'Courier'),
                               ('FONTSIZE', (0, 0), (-1, -1), 8)]))
        data_len = len(data)
        for each in range(data_len):
            if each % 2 == 0:
                bg_color = colors.whitesmoke
            else:
                bg_color = colors.lightgrey

        f.setStyle(TableStyle(
            [('BACKGROUND', (0, each), (-1, each), bg_color)]))
        f_data_withoutD.setStyle(TableStyle(
            [('BACKGROUND', (0, each), (-1, each), bg_color)]))
        aW = 540
        aH = 720
        w, h = header.wrap(aW, aH)
        header.drawOn(c, 48, aH)
        header.drawOn(c1, 48, aH)
        aH = aH - h
        w, h = f.wrap(aW, aH)
        w, h = f_data_withoutD.wrap(aW, aH)
        f.drawOn(c, 48, aH-h)
        f_data_withoutD.drawOn(c1, 48, aH-h)
        c.showPage()
        c1.showPage()
        c.save()
        c1.save()

    def cleanexcel(self):
        # self.text = self.number_var.get()
        # self.df['Lowerbound'] = self.df["0_p_ÖL    In"] - 0.50
        self.df['Lowerbound'] = self.df.iloc[:, 2] - \
            (float(self.entrylist_label[0].get()))
        # self.df['Upperbound'] = self.df["0_p_ÖL    In"] + 0.50
        self.df['Upperbound'] = self.df.iloc[:, 2] + \
            (float(self.entrylist_label[0].get()))
        print(self.df.head(10))
        # self.ser_sensor1 = pd.Series(self.df.iloc[:, 9])
        # self.ser_sensor2 = pd.Series(self.df.iloc[:, 10])
        # self.ser_sensor3 = pd.Series(self.df.iloc[:, 11])
        # self.ser_sensor4 = pd.Series(self.df.iloc[:, 12])
        # self.ser_sensor5 = pd.Series(self.df.iloc[:, 13])
        # self.ser_sensor6 = pd.Series(self.df.iloc[:, 14])
        # self.ser_sensor7 = pd.Series(self.df.iloc[:, 15])
        # self.ser_sensor8 = pd.Series(self.df.iloc[:, 16])
        # self.ser_sensor9 = pd.Series(self.df.iloc[:, 17])
        # self.ser_sensor10 = pd.Series(self.df.iloc[:, 18])

        self.ser1_Lowerbound = pd.Series(self.df["Lowerbound"])
        self.ser1_Upperbound = pd.Series(self.df["Upperbound"])
        self.file1 = open('Result.txt', 'w')
        self.totaltruevalues = []
        print((int(self.entrylist_label2[0].get()))+1)
        for i in range(int(self.entrylist_label1[0].get())):
            self.df['sensor' + str(i+1)] = (self.df.iloc[:, (int(self.entrylist_label2[0].get()))+1+i]
                                            ).between(self.ser1_Lowerbound, self.ser1_Upperbound)
            self.totaltruevalues.append(
                self.df['sensor' + str(i+1)].value_counts())
            self.df['sensor' +
                    str(i+1)] = np.where(self.df['sensor' + str(i+1)] == True, 1, 0)
            # print (i)
        self.file1.write('\n'.join(map(str, self.totaltruevalues)))
        self.file1.close()
        self.df.to_csv("Results.csv", index=False, header=True)
        d = {}
        for i in range(int(self.entrylist_label1[0].get())):
            # self.dict['falsesen'+ str(i+1)] = pd.DataFrame()
            d['falsesen' + str(i+1)
              ] = self.df[self.df['sensor' + str(i+1)] == 0]
            # print( self.dict['falsesen'+ str(i)].head())
            # print('\n')
        self.df_false_sen_1 = pd.DataFrame(d['falsesen1'])
        self.df_false_sen_2 = pd.DataFrame(d['falsesen2'])
        self.df_false_sen_3 = pd.DataFrame(d['falsesen3'])
        self.df_false_sen_4 = pd.DataFrame(d['falsesen4'])
        self.df_false_sen_5 = pd.DataFrame(d['falsesen5'])
        self.df_false_sen_6 = pd.DataFrame(d['falsesen6'])
        self.df_false_sen_7 = pd.DataFrame(d['falsesen7'])
        self.df_false_sen_8 = pd.DataFrame(d['falsesen8'])
        self.df_false_sen_9 = pd.DataFrame(d['falsesen9'])
        self.df_false_sen_10 = pd.DataFrame(d['falsesen10'])
        # false value of a sensors are seperated into different DF. 10 different df are created, startingname of  df is self.df_false_sen_1
        # print(self.df_false_sen_1.iloc[:, 9].head())
        # print(self.df_false_sen_2.head())
        # print(self.df_false_sen_3.head())
        # print(self.df_false_sen_4.head())
        self.df_false_sen_3.to_excel('falsesensor1.xlsx', index=0, header=True)

        # self.df.excel("output.xlsx", sep=';', encoding='latin-1')
        print("Completed")
        # self.plt_first4sensors()

    def plt_first4sensors(self):

        fig, axes = plt.subplots(nrows=2, ncols=2)
        self.df_false_sen_1.plot(
            x="Time", y='1_Wika R1 0-50', linestyle='-.', color='red', ax=axes[0, 0])
        self.df_false_sen_1.plot(
            x="Time", y='Lowerbound', linewidth=2, color='blue', ax=axes[0, 0])
        self.df_false_sen_1.plot(
            x="Time", y='Upperbound', linewidth=2, color='green', ax=axes[0, 0])

        self.df_false_sen_2.plot(
            x="Time", y='1.1_Wika R1 0-50', linestyle='-.', color='red', ax=axes[0, 1])
        self.df_false_sen_2.plot(
            x="Time", y='Lowerbound', linewidth=2, color='blue', ax=axes[0, 1])
        self.df_false_sen_2.plot(
            x="Time", y='Upperbound', linewidth=2, color='green', ax=axes[0, 1])

        self.df_false_sen_3.plot(
            x="Time", y='1.2_Dunan HIB50', linestyle='-.', color='red', ax=axes[1, 0])
        self.df_false_sen_3.plot(
            x="Time", y='Lowerbound', linewidth=2, color='blue', ax=axes[1, 0])
        self.df_false_sen_3.plot(
            x="Time", y='Upperbound', linewidth=2, color='green', ax=axes[1, 0])

        self.df_false_sen_4.plot(
            x="Time", y='1.3_Dunan HIB50', linestyle='-.', color='red', ax=axes[1, 1])
        self.df_false_sen_4.plot(
            x="Time", y='Lowerbound', linewidth=2, color='blue', ax=axes[1, 1])
        self.df_false_sen_4.plot(
            x="Time", y='Upperbound', linewidth=2, color='green', ax=axes[1, 1])
        # self.plt_sensors5to8()
        #plt.show()

    def plt_sensors5to8(self):
        fig, axes1 = plt.subplots(nrows=2, ncols=2)
        self.df_false_sen_5.plot(
            x="Time", y='1.4_Dunan HIB50', linestyle='-.', color='red', ax=axes1[0, 0])
        self.df_false_sen_5.plot(
            x="Time", y='Lowerbound', linewidth=2, color='blue', ax=axes1[0, 0])
        self.df_false_sen_5.plot(
            x="Time", y='Upperbound', linewidth=2, color='green', ax=axes1[0, 0])

        self.df_false_sen_6.plot(
            x="Time", y='1.5_Dunan HIB50', linestyle='-.', color='red', ax=axes1[0, 1])
        self.df_false_sen_6.plot(
            x="Time", y='Lowerbound', linewidth=2, color='blue', ax=axes1[0, 1])
        self.df_false_sen_6.plot(
            x="Time", y='Upperbound', linewidth=2, color='green', ax=axes1[0, 1])

        self.df_false_sen_7.plot(
            x="Time", y='1.6_Dunan HIB50', linestyle='-.', color='red', ax=axes1[1, 0])
        self.df_false_sen_7.plot(
            x="Time", y='Lowerbound', linewidth=2, color='blue', ax=axes1[1, 0])
        self.df_false_sen_7.plot(
            x="Time", y='Upperbound', linewidth=2, color='green', ax=axes1[1, 0])

        self.df_false_sen_8.plot(
            x="Time", y='1.7_Dunan HIB50', linestyle='-.', color='red', ax=axes1[1, 1])
        self.df_false_sen_8.plot(
            x="Time", y='Lowerbound', linewidth=2, color='blue', ax=axes1[1, 1])
        self.df_false_sen_8.plot(
            x="Time", y='Upperbound', linewidth=2, color='green', ax=axes1[1, 1])
        # self.plt_last2sensors()
        #plt.show()

    def plt_last2sensors(self):
        fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1)
        self.df_false_sen_9.plot(
            x="Time", y='1.8_Dunan HIB50', linestyle='-.', color='red', ax=ax1)
        self.df_false_sen_9.plot(
            x="Time", y='Lowerbound', linewidth=2, color='blue', ax=ax1)
        self.df_false_sen_9.plot(
            x="Time", y='Upperbound', linewidth=2, color='green', ax=ax1)

        self.df_false_sen_10.plot(
            x="Time", y='1.9_Dunan HIB50', linestyle='-.', color='red', ax=ax2)
        self.df_false_sen_10.plot(
            x="Time", y='Lowerbound', linewidth=2, color='blue', ax=ax2)
        self.df_false_sen_10.plot(
            x="Time", y='Upperbound', linewidth=2, color='green', ax=ax2)
        #plt.show()


window = WindowApp()
window.mainloop()
