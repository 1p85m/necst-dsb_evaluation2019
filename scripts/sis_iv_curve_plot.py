#!/usr/bin/env python3

name = 'sis_iv_curve_plot'

import os, sys
import matplotlib.pyplot as plt
import std_msgs.msg
import pandas

import necstdb

parser = argparse.ArgumentParser(description = 'search optical Lo Att voltage value')

parser.add_argument('file_name', type = str, help = 'saved file name when measure I-V curve')
parser.add_argument('sive_name', type = str, help = 'set saving I-V graph file name')

args = parser.parse_args()

db = necstdb.necstdb()
db.open(args.file_name)

d = db.read_as_pandas()
d['time'] = pandas.to_datetime(d['time'], unit='s')
d['data'] = [_[0][data] for _ in d['msgs']]
d2 = d.set_index(['topic', 'time']).sort_index()

dd = pandas.concat(
    [
        d2.loc['/dsb_evaluation2019/sis/v'][['data']].rename(columns={'data': 'V'}).astype(float).resample('0.1S').mean(),
        d2.loc['/dsb_evaluation2019/sis/i'][['data']].rename(columns={'data': 'I'}).astype(float).resample('0.1S').mean(),
    ],
    axis = 1,
)

#under the i-v graph plot

fig = matplotlib.pyplot.figure(figsize=(7, 6))
ax = [fig.add_subplot(1, 1, i) for i in range(1)]
ax[0].plot(dd['V'], dd['I'], '.')
ax[0].set_title('I-V')
[_.set_xlabel('Voltage (mV)') for _ in ax]
[_.set_ylabel('Current (uA)') for _ in ax]
[_.grid(True, linestyle=':') for _ in ax]

plt.savefig(args.save_name)
plt.show()
