SDK 错误码对照表
====================

.. csv-table:: 
    :header-rows: 1
    :name: 接口返回值错误码对照表
    :widths: 10 20 30

    "errcode","描述","处理方式"
    "-1","其他错误","联系售后工程师查看控制器日志"
    "0","调用成功",""
    "3","接口参数个数不一致","检查接口参数个数"
    "4","接口参数值异常","检查参数值类型或范围"
    "8","轨迹文件打开失败","检查TPD轨迹文件是否存在或轨迹名是否正确"
    "14","接口执行失败","检查web界面是否报故障或状态反馈是否报故障"
    "18","机器人程序正在运行，请先停止","先停止程序，再进行其他操作"
    "25","数据异常，计算失败","重新标定或辨识"
    "28","逆运动学计算结果异常","检查位姿是否合理"
    "29","ServoJ关节超限","检查关节数据是否在合理范围"
    "30","不可复位故障，请断电重启控制箱","请断电重启控制箱"
    "34","工件号错误","请检查工件号是否合理"
    "36","文件名过长","请缩减文件名长度"
    "38","奇异位姿，计算失败","请更换位姿"
    "64","未加入指令队列","联系售后工程师查看控制器日志"
    "66","整圆/螺旋线指令中间点1错误","检查中间点1数据是否正确"
    "67","整圆/螺旋线指令中间点2错误","检查中间点2数据是否正确"
    "68","整圆/螺旋线指令中间点3错误","检查中间点3数据是否正确"
    "69","圆弧指令中间点错误","检查中间点数据是否正确"
    "70","圆弧指令目标点错误","检查目标点数据是否正确"
    "73","夹爪运动报错","检查夹爪通信状态是否正常"
    "74","直线指令点错误","检查点位数据是否正确"
    "75","通道错误","检查IO编号是否在范围内"
    "76","等待超时","检查IO信号是否输入或接线是否正确"
    "82","TPD指令点错误","重新记录示教轨迹"
    "83","TPD指令工具与当前工具不符","更改为TPD示教时所用的工具坐标系"
    "94","样条指令点错误","检查点位数据是否正确"
    "108","螺旋线指令起点错误","检查起点数据是否正确"
    "112","给定位姿无法到达","检查目标位姿是否合理"
