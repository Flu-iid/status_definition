from task.static_definitions import status_code_definition_en_list as d_en, status_code_definition_fa_list as d_fa

# with open("output_fa.csv", "r") as fa:
#     with open("output_en.csv", "r") as en:
#         with open("result.csv", "+a") as foo:
#             for l in fa.readlines():


import pandas as pd
import numpy as np

df_en, df_fa = pd.read_csv("output_en.csv"), pd.read_csv("output_fa.csv")
df_fa["code"] = df_fa["code"].apply(int)

code90 = np.array(list(d_fa.keys()))
code90 = code90[code90 > 90000]
code90 = code90[code90 < 91000]
# print(code90)

code10 = np.array(list(d_fa.keys()))
code10 = code10[code10 > 10000]
code10 = code10[code10 < 11000]
# print(code10)

code_extra = [20010000, 20015000, 20028000, 9101]


df_fa["code10"] = [(10*10**3+i) if (10*10**3+i) in d_fa.keys()
                   else np.nan for i in df_fa["code"]]
df_fa["prior10_fa"] = [d_fa[10*10**3+i] if (10*10**3+i) in d_fa.keys()
                       else np.nan for i in df_fa["code"]]
df_en["prior10_en"] = [d_en[10*10**3+i] if (10*10**3+i) in d_en.keys()
                       else np.nan for i in df_en["code"]]
df_fa["code90"] = [(90*10**3+i) if (90*10**3+i) in d_fa.keys()
                   else np.nan for i in df_fa["code"]]
df_fa["prior90_fa"] = [d_fa[90*10**3+i] if (90*10**3+i) in d_fa.keys()
                       else np.nan for i in df_fa["code"]]
df_en["prior90_en"] = [d_en[90*10**3+i] if (90*10**3+i) in d_en.keys()
                       else np.nan for i in df_en["code"]]
df_fa["prior_fa"] = [d_fa[i] if i in d_fa.keys() else np.nan for i in df_fa["code"]]
df_en["prior_en"] = [d_en[i] if i in d_en.keys() else np.nan for i in df_en["code"]]
df_fa["code_extra"] = [None]*len(df_fa)
df_fa["prior_extra_en"] = [None]*len(df_fa)
df_fa["prior_extra_fa"] = [None]*len(df_fa)
df_total = df_fa.merge(df_en)
for i in code_extra:
    df_total.loc[len(df_total)] = [np.nan]*len(df_total.columns)
    df_total["code_extra"].loc[len(df_total)-1] = i
new_col = ['code', 'title_en', 'description_en', 'title_fa', 'description_fa', 'prior_en', 'prior_fa', 'code90',
           'prior90_en', 'prior90_fa', 'code10',  'prior10_en', 'prior10_fa', 'code_extra', "prior_extra_en", "prior_extra_fa"]
df_total = df_total[new_col]
print(df_total)
print(df_total.columns)

df_total.to_csv("output.csv")
