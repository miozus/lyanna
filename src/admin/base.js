import UIkit from 'uikit';
import Icons from 'uikit/dist/js/uikit-icons';

// 加载图标插件
UIkit.use(Icons);

// 可以从导入的UIkit引用调用组件
UIkit.notification('Hello world.');

// E1: UIkit模板安装和初始化模板，yarn install, yarn run start