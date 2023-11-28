export function option_mapping(i) {
  if (i >= 1001) {
    let option1001 = {
      title: {
        text: "Stacked Line",
        textStyle: {},
      },
      tooltip: {
        trigger: "axis",
      },
      legend: {
        data: ["Email", "Union Ads", "Video Ads", "Direct", "Search Engine"],
      },
      grid: {
        left: "3%",
        right: "4%",
        bottom: "3%",
        containLabel: true,
      },
      toolbox: {
        feature: {
          saveAsImage: {},
        },
      },
      xAxis: {
        type: "category",
        boundaryGap: false,
        data: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
      },
      yAxis: {
        type: "value",
      },
      series: [
        {
          name: "Email",
          type: "line",
          stack: "Total",
          data: [120, 132, 101, 134, 90, 230, 210],
        },
        {
          name: "Union Ads",
          type: "line",
          stack: "Total",
          data: [220, 182, 191, 234, 290, 330, 310],
        },
        {
          name: "Video Ads",
          type: "line",
          stack: "Total",
          data: [150, 232, 201, 154, 190, 330, 410],
        },
        {
          name: "Direct",
          type: "line",
          stack: "Total",
          data: [320, 332, 301, 334, 390, 330, 320],
        },
        {
          name: "Search Engine",
          type: "line",
          stack: "Total",
          data: [820, 932, 901, 934, 1290, 1330, 1320],
        },
      ],
    };
    return option1001;
  }
  // 返回默认值，保证不报错
  return {
    title: {
      textStyle: {},
    },
    legend: {},
    xAxis: {
      type: "category",
      data: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    },
    yAxis: {
      type: "value",
    },
    series: [
      {
        data: [150, 230, 224, 218, 135, 147, 260],
        type: "line",
      },
    ],
  };
}

export function line_option(p_title = "", p_xAxis = [], y_serials = []) {
  let result = [];
  y_serials.map((item) => {
    item["itemStyle"] = {
      normal: {
        label: {
          show: true, //开启显示
          position: "top", //在上方显示
          textStyle: {
            //数值样式
            color: "black",
            fontSize: 12,
          },
        },
      },
    };
    result.push(item);
  });
  y_serials = result;

  let option = {
    title: {
      text: p_title,
      left: "center",
    },
    tooltip: {
      trigger: "axis",
    },
    legend: {
      data: [],
    },
    toolbox: {
      show: true,
      feature: {
        mark: { show: true },
        dataView: { show: true, readOnly: false },
        restore: { show: true },
        saveAsImage: { show: true },
      },
    },
    xAxis: {
      type: "category",
      boundaryGap: false,
      data: p_xAxis,
    },
    yAxis: {
      type: "value",
    },
    series: y_serials,
  };
  return option;
}
export function pie_option(p_title = "", y_data = []) {
  return option;
}

export function rose_option(p_title = "", y_data = []) {
  let option = {
    title: {
      text: p_title,
      left: "left",
    },
    toolbox: {
      show: true,
      feature: {
        mark: { show: true },
        dataView: { show: true, readOnly: false },
        restore: { show: true },
        saveAsImage: { show: true },
      },
    },
    series: [
      {
        name: p_title,
        type: "pie",
        radius: [50, 250],
        center: ["50%", "50%"],
        roseType: "area",
        itemStyle: {
          borderRadius: 8,
        },
        data: y_data,
      },
    ],
  };
  return option;
}

export function relation_option(p_nodes = [], p_links = [], p_categories = []) {
  let option = {
    title: {
      text: "当前校企合作关系",
      textStyle: {
        color: "white",
      },
      left: "30px",
      top: "20px",
    },
    tooltip: {
      show: true,
    },
    legend: {
      show: false,
    },
    xAxis: {
      show: false,
    },
    yAxis: {
      show: false,
    },
    grid: {
      top: "80px",
    },
    series: [
      {
        type: "graph",
        // 是否开启鼠标缩放和平移漫游。默认不开启。如果只想要开启缩放或者平移，可以设置成 'scale' 或者 'move'。设置成 true 为都开启
        roam: true,
        // 是否在鼠标移到节点上的时候突出显示节点以及节点的边和邻接节点。[ default: false ]
        focusNodeAdjacency: true,
        // 力引导布局相关的配置项，力引导布局是模拟弹簧电荷模型在每两个节点之间添加一个斥力，每条边的两个节点之间添加一个引力，每次迭代节点会在各个斥力和引力的作用下移动位置，多次迭代后节点会静止在一个受力平衡的位置，达到整个模型的能量最小化。
        force: {
          // 力引导布局的结果有良好的对称性和局部聚合性，也比较美观。
          // [ default: 50 ]节点之间的斥力因子(关系对象之间的距离)。支持设置成数组表达斥力的范围，此时不同大小的值会线性映射到不同的斥力。值越大则斥力越大
          repulsion: 200,
          // [ default: 30 ]边的两个节点之间的距离(关系对象连接线两端对象的距离,会根据关系对象值得大小来判断距离的大小)，
          edgeLength: [120, 100],
          // 这个距离也会受 repulsion。支持设置成数组表达边长的范围，此时不同大小的值会线性映射到不同的长度。值越小则长度越长。如下示例:
          // 值最大的边长度会趋向于 10，值最小的边长度会趋向于 50      edgeLength: [10, 50]
        },
        // 图的布局。[ default: 'none' ]
        layout: "force",
        // 'none' 不采用任何布局，使用节点中提供的 x， y 作为节点的位置。
        // 'circular' 采用环形布局;'force' 采用力引导布局.
        // 标记的图形
        symbol: "circle",
        // 关系边的公用线条样式。其中 lineStyle.color 支持设置为'source'或者'target'特殊值，此时边会自动取源节点或目标节点的颜色作为自己的颜色。
        normal: {
          lineStyle: {
            // 线的颜色[ default: '#aaa' ]
            color: "#fff",
            // 线宽[ default: 1 ]
            width: 1,
            // 线的类型[ default: solid实线 ]   'dashed'虚线    'dotted'
            type: "solid",
            // 图形透明度。支持从 0 到 1 的数字，为 0 时不绘制该图形。[ default: 0.5 ]
            opacity: 0.5,
            // 边的曲度，支持从 0 到 1 的值，值越大曲度越大。[ default: 0 ]
            curveness: 0.5,
          },
        },
        // 关系对象上的标签
        label: {
          normal: {
            // 是否显示标签
            show: true,
            // 标签位置:'top''left''right''bottom''inside''insideLeft''insideRight''insideTop''insideBottom''insideTopLeft''insideBottomLeft''insideTopRight''insideBottomRight'
            position: "inside",
            // 文本样式
            textStyle: {
              fontSize: 16,
              color: "white",
            },
          },
        },
        // 连接两个关系对象的线上的标签
        edgeLabel: {
          normal: {
            show: true,
            textStyle: {
              // fontSize: 14
            },
            // 标签内容
            formatter: function (param) {
              return param.data.category;
            },
          },
        },
        data: p_nodes,
        // 节点分类的类目，可选。如果节点有分类的话可以通过 data[i].category 指定每个节点的类目，类目的样式会被应用到节点样式上。图例也可以基于categories名字展现和筛选。
        categories: p_categories,
        // 节点间的关系数据
        links: p_links,
      },
    ],
  };
  return option;
}
