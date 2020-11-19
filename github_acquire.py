# Code module to acquire the github readmes:

"""
A module for obtaining repo readme and language data from the github API.

Before using this module, read through it, and follow the instructions marked
TODO.

After doing so, run it like this:

    python acquire.py

To create the `data.json` file that contains the data.
"""
import os
import json
from typing import Dict, List, Optional, Union, cast
import requests

from env import github_token, github_username

# TODO: Make a github personal access token.
#     1. Go here and generate a personal access token https://github.com/settings/tokens
#        You do _not_ need select any scopes, i.e. leave all the checkboxes unchecked
#     2. Save it in your env.py file under the variable `github_token`
# TODO: Add your github username to your env.py file under the variable `github_username`
# TODO: Add more repositories to the `REPOS` list below.

REPOS = [
    'ytdl-org/youtube-dl',
    'jackfrued/Python-100-Days',
    'pallets/flask',
    'django/django',
    'TheAlgorithms/Python',
    'public-apis/public-apis',
    'tensorflow/models',
    'vinta/awesome-python',
    'donnemartin/system-design-primer',
    'nvbn/thefuck',
    'josephmisiti/awesome-machine-learning',
    'psf/requests',
    'scikit-learn/scikit-learn',
    'minimaxir/big-list-of-naughty-strings',
    'httpie/httpie',
    'soimort/you-get',
    'ageitgey/face_recognition',
    'ansible/ansible',
    'scrapy/scrapy',
    'home-assistant/core',
    'huggingface/transformers',
    'isocpp/CppCoreGuidelines',
    'shadowsocks/shadowsocks',
    'python/cpython',
    'deepfakes/faceswap',
    'testerSunshine/12306',
    '0voice/interview_internal_reference',
    'apache/incubator-superset',
    'XX-net/XX-Net',
    '521xueweihan/HelloGitHub',
    'getsentry/sentry',
    'apachecn/AiLearning',
    'fighting41love/funNLP',
    'certbot/certbot',
    '3b1b/manim',
    'localstack/localstack',
    'floodsung/Deep-Learning-Papers-Reading-Roadmap',
    'faif/python-patterns',
    'google-research/bert',
    'pandas-dev/pandas',
    'tornadoweb/tornado',
    'pypa/pipenv',
    'CorentinJ/Real-Time-Voice-Cloning',
    '0xAX/linux-insides',
    'iperov/DeepFaceLab',
    'donnemartin/data-science-ipython-notebooks',
    'mitmproxy/mitmproxy',
    'ycm-core/YouCompleteMe',
    'donnemartin/interactive-coding-challenges',
    'chubin/cheat.sh',
    'tornadoweb/tornado',
    'pypa/pipenv',
    'iperov/DeepFaceLab',
    'geekcomputers/Python',
    'docker/compose',
    'donnemartin/data-science-ipython-notebooks',
    'littlecodersh/ItChat',
    'mitmproxy/mitmproxy',
    'donnemartin/interactive-coding-challenges',
    'trailofbits/algo',
    'psf/black',
    'matterport/Mask_RCNN',
    'keon/algorithms',
    'swisskyrepo/PayloadsAllTheThings',
    'sqlmapproject/sqlmap',
    'encode/django-rest-framework',
    'apache/airflow',
    'yunjey/pytorch-tutorial',
    'd2l-ai/d2l-zh',
    'eriklindernoren/ML-From-Scratch',
    'binux/pyspider',
    'instillai/TensorFlow-Course',
    'numpy/numpy',
    'tqdm/tqdm',
    'deezer/spleeter',
    'magenta/magenta',
    'celery/celery',
    'pytorch/examples',
    'ipython/ipython',
    'charlax/professional-programming',
    'binux/pyspider',
    'instillai/TensorFlow-Course',
    'numpy/numpy',
    'reddit-archive/reddit',
    'deezer/spleeter',
    'magenta/magenta',
    'celery/celery',
    'pytorch/examples',
    'ipython/ipython',
    'charlax/professional-programming',
    'mwaskom/seaborn',
    'coleifer/peewee',
    'searx/searx',
    'python-pillow/Pillow',
    'eriklindernoren/PyTorch-GAN',
    'sfyc23/EverydayWechat',
    'mlflow/mlflow',
    'django-cms/django-cms',
    'dbader/schedule',
    'harelba/q',
    'lauris/awesome-scala',
    'pytorch/vision',
    'EpistasisLab/tpot',
    'scipy/scipy',
    'facebookresearch/visdom',
    'clips/pattern',
    'lk-geimfari/awesomo',
    'eriklindernoren/Keras-GAN',
    'lyhue1991/eat_tensorflow2_in_30_days',
    'sylnsfar/qrcode',
    'MobSF/Mobile-Security-Framework-MobSF',
    'amueller/word_cloud',
    'ankitects/anki',
    'hoochanlon/w3-goto-world',
    'keras-team/autokeras',
    'NVIDIA/vid2vid',
    'pirate/ArchiveBox',
    'sympy/sympy',
    'seatgeek/fuzzywuzzy',
    'aws/serverless-application-model',
    'programthink/zhao',
    'vipstone/faceai',
    'dask/dask',
    'pwxcoo/chinese-xinhua',
    'pydanny/cookiecutter-django',
    'Delgan/loguru',
    'sloria/TextBlob',
    'aws/chalice',
    'Cadene/pretrained-models.pytorch',
    'pyinstaller/pyinstaller',
    's0md3v/Photon',
    'benoitc/gunicorn',
    'Yorko/mlcourse.ai',
    'samshadwell/TrumpScript',
    'Gallopsled/pwntools',
    'pallets/jinja',
    'rq/rq',
    'tweepy/tweepy',
    'MagicStack/uvloop',
    'uber/ludwig',
    'netbox-community/netbox',
    'rbgirshick/py-faster-rcnn',
    'openai/universe',
    'docopt/docopt',
    'hardikvasa/google-images-download',
    'wangshub/Douyin-Bot',
    'frappe/erpnext',
    'Yelp/elastalert',
    'Zulko/moviepy',
    'deepmind/pysc2',
    'bottlepy/bottle',
    'miguelgrinberg/flasky',
    '30-seconds/30-seconds-of-python',
    'donnemartin/gitsome',
    'cyrus-and/gdb-dashboard',
    'EZFNDEV/EZFN',
    'matrix-org/synapse',
    'ReFirmLabs/binwalk',
    'bbfamily/abu',
    'nodejs/node-gyp',
    'dabeaz-course/practical-python',
    'larsenwork/monoid',
    'pypa/pip',
    'lanpa/tensorboardX',
    'facebookresearch/ParlAI',
    'giampaolo/psutil',
    'iterative/dvc',
    'Urinx/WeixinBot',
    'pytest-dev/pytest',
    'mopidy/mopidy',
    'pyro-ppl/pyro',
    'a1studmuffin/SpaceshipGenerator',
    'bregman-arie/devops-exercises',
    'yandex/gixy',
    'fchollet/deep-learning-models',
    'brightmart/text_classification',
    'OpenMined/PySyft',
    'instillai/machine-learning-course',
    'prompt-toolkit/python-prompt-toolkit',
    'paramiko/paramiko',
    'facebook/react-native',
    'twbs/bootstrap',
    'vuejs/vue',
    'facebook/create-react-app',
    'd3/d3',
    'trekhleb/javascript-algorithms',
    'facebook/react',
    'axios/axios',
    'airbnb/javascript',
    'freeCodeCamp/freeCodeCamp',
    'jquery/jquery',
    'angular/angular.js',
    'mrdoob/three.js',
    'vercel/next.js',
    'goldbergyoni/nodebestpractices',
    'FortAwesome/Font-Awesome',
    'webpack/webpack',
    'nodejs/node',
    'mui-org/material-ui',
    '30-seconds/30-seconds-of-code',
    'chartjs/Chart.js',
    'adam-p/markdown-here',
    'hakimel/reveal.js',
    'Semantic-Org/Semantic-UI',
    'atom/atom',
    'socketio/socket.io',
    'gothinkster/realworld',
    'expressjs/express',
    'typicode/json-server',
    'awesome-selfhosted/awesome-selfhosted',
    'gatsbyjs/gatsby',
    'ReactTraining/react-router',
    'lodash/lodash',
    'moment/moment',
    'yangshun/tech-interview-handbook',
    'meteor/meteor',
    'scutan90/DeepLearning-500-questions',
    'ryanmcdermott/clean-code-javascript',
    'h5bp/html5-boilerplate',
    'resume/resume.github.com',
    'babel/babel',
    'prettier/prettier',
    'NARKOZ/hacker-scripts',
    'nwjs/nw.js',
    'yarnpkg/yarn',
    'Dogfalo/materialize',
    'jaywcjlove/awesome-mac',
    'sveltejs/svelte',
    'serverless/serverless',
    'azl397985856/leetcode',
    'TryGhost/Ghost',
    'mermaid-js/mermaid',
    'juliangarnier/anime',
    'parcel-bundler/parcel',
    'Unitech/pm2',
    'ColorlibHQ/AdminLTE',
    'mozilla/pdf.js',
    'impress/impress.js',
    'leonardomso/33-js-concepts',
    'algorithm-visualizer/algorithm-visualizer',
    'hexojs/hexo',
    'strapi/strapi',
    'iamkun/dayjs',
    'chinese-poetry/chinese-poetry',
    'sahat/hackathon-starter',
    'styled-components/styled-components',
    'adobe/brackets',
    'gulpjs/gulp',
    'nuxt/nuxt.js',
    'alvarotrigo/fullPage.js',
    'koajs/koa',
    'quilljs/quill',
    'Marak/faker.js',
    'Leaflet/Leaflet',
    'zenorocha/clipboard.js',
    'videojs/video.js',
    'photonstorm/phaser',
    'immutable-js/immutable-js',
    'RocketChat/Rocket.Chat',
    'jondot/awesome-react-native',
    'preactjs/preact',
    'tastejs/todomvc',
    'dcloudio/uni-app',
    'yangshun/front-end-interview-handbook',
    'NervJS/taro',
    'react-boilerplate/react-boilerplate',
    'kenwheeler/slick',
    'caolan/async',
    'jashkenas/backbone',
    'vuejs/vue-cli',
    'poteto/hiring-without-whiteboards',
    'sampotts/plyr',
    'segmentio/nightmare',
    'laurent22/joplin',
    'react-bootstrap/react-bootstrap',
    'YMFE/yapi',
    'vuejs/vue-devtools',
    'swagger-api/swagger-ui',
    'ruanyf/es6tutorial',
    'bilibili/flv.js',
    'immerjs/immer',
    'jaredhanson/passport',
    'parse-community/parse-server',
    'verekia/js-stack-from-scratch',
    'localForage/localForage',
    'jamiebuilds/the-super-tiny-compiler',
    'jorgebucaran/hyperapp',
    'viatsko/awesome-vscode',
    'lovell/sharp',
    'avajs/ava',
    'vuejs/vuepress',
    'necolas/react-native-web',
    'highlightjs/highlight.js',
    'getredash/redash',
    'eslint/eslint',
    'goldfire/howler.js',
    'reduxjs/reselect',
    'Popmotion/popmotion',
    'jhipster/generator-jhipster',
    'Binaryify/NeteaseCloudMusicApi',
    'BoostIO/Boostnote',
    'marktext/marktext',
    'wekan/wekan',
    'benweet/stackedit',
    'fabricjs/fabric.js',
    'graphql/graphql-js',
    'zhaoolee/ChromeAppHeroes',
    'vuejs/vue-router',
    'julianshapiro/velocity',
    'facebook/flux',
    'vercel/pkg',
    'less/less.js',
    'js-cookie/js-cookie',
    'portainer/portainer',
    'quasarframework/quasar',
    'defunkt/jquery-pjax',
    'angular/material',
    'validatorjs/validator.js',
    'fastify/fastify',
    'git-tips/tips',
    'popperjs/popper-core',
    'JacksonTian/fks',
    'nosir/cleave.js',
    'eggjs/egg',
    'twitter/typeahead.js',
    'HelloZeroNet/ZeroNet',
    'sideway/joi',
    'winstonjs/winston',
    'alsotang/node-lessons',
    'mojs/mojs',
    'framework7io/framework7',
    'docsifyjs/docsify',
    'handlebars-lang/handlebars.js',
    'remoteintech/remote-jobs',
    'reduxjs/redux-thunk',
    'youzan/vant',
    'mysqljs/mysql',
    'nuysoft/Mock',
    'hubotio/hubot',
    'jamiebuilds/react-loadable',
    'eligrey/FileSaver.js',
    'ruanyf/react-demos',
    'websockets/ws',
    'visionmedia/superagent',
    'enyo/dropzone',
    'chalk/chalk',
    'bower/bower',
    'statsd/statsd',
    'dvajs/dva',
    'adam-golab/react-developer-roadmap',
    'Kong/insomnia',
    'yabwe/medium-editor',
    'svg/svgo',
    'chaozh/awesome-blockchain-cn',
    'kriskowal/q',
    'wagerfield/parallax',
    'jasmine/jasmine',
    'facebook/relay',
    'ccxt/ccxt',
    'jsdom/jsdom',
    'alpinejs/alpine',
    'phobal/ivideo',
    'krisk/Fuse',
    'gaearon/react-hot-loader',
    'gpujs/gpu.js',
    'http-party/node-http-proxy',
    'greensock/GSAP',
    'Semantic-Org/Semantic-UI-React',
    'Automattic/wp-calypso',
    'VerbalExpressions/JSVerbalExpressions',
    'artf/grapesjs',
    '1995parham/github-do-not-ban-us',
    'appium/appium',
    'Tencent/vConsole',
    'lutzroeder/netron',
    'aframevr/aframe',
    'pomber/git-history',
    'uxsolutions/bootstrap-datepicker',
    'you-dont-need/You-Dont-Need-Lodash-Underscore',
    'nondanee/UnblockNeteaseMusic',
    'kamranahmedse/driver.js',
    'nhn/tui.editor',
    'erikras/react-redux-universal-hot-example',
    'sweetalert2/sweetalert2',
    'docker/kitematic',
    'gruntjs/grunt',
    'paperjs/paper.js',
    'emotion-js/emotion',
    'zalmoxisus/redux-devtools-extension',
    'louischatriot/nedb',
    'alpinejs/alpine',
    'rwaldron/johnny-five',
    'phobal/ivideo',
    'gaearon/react-hot-loader',
    'gpujs/gpu.js',
    'http-party/node-http-proxy',
    'greensock/GSAP',
    'Semantic-Org/Semantic-UI-React',
    'Automattic/wp-calypso',
    'VerbalExpressions/JSVerbalExpressions',
    'scottjehl/Respond',
    'jwagner/smartcrop.js',
    'Tencent/omi',
    'DrkSephy/es6-cheatsheet',
    'jquense/yup',
    'krisk/Fuse',
    'NodeBB/NodeBB',
    'shelljs/shelljs',
    'aurelia/framework',
    'RelaxedJS/ReLaXed',
    ]

headers = {"Authorization": f"token {github_token}", "User-Agent": github_username}

if headers["Authorization"] == "token " or headers["User-Agent"] == "":
    raise Exception(
        "You need to follow the instructions marked TODO in this script before trying to use it"
    )


def github_api_request(url: str) -> Union[List, Dict]:
    response = requests.get(url, headers=headers)
    response_data = response.json()
    if response.status_code != 200:
        raise Exception(
            f"Error response from github api! status code: {response.status_code}, "
            f"response: {json.dumps(response_data)}"
        )
    return response_data


def get_repo_language(repo: str) -> str:
    url = f"https://api.github.com/repos/{repo}"
    repo_info = github_api_request(url)
    if type(repo_info) is dict:
        repo_info = cast(Dict, repo_info)
        return repo_info.get("language", None)
    raise Exception(
        f"Expecting a dictionary response from {url}, instead got {json.dumps(repo_info)}"
    )


def get_repo_contents(repo: str) -> List[Dict[str, str]]:
    url = f"https://api.github.com/repos/{repo}/contents/"
    contents = github_api_request(url)
    if type(contents) is list:
        contents = cast(List, contents)
        return contents
    raise Exception(
        f"Expecting a list response from {url}, instead got {json.dumps(contents)}"
    )


def get_readme_download_url(files: List[Dict[str, str]]) -> str:
    """
    Takes in a response from the github api that lists the files in a repo and
    returns the url that can be used to download the repo's README file.
    """
    for file in files:
        if file["name"].lower().startswith("readme"):
            return file["download_url"]
    return ""


def process_repo(repo: str) -> Dict[str, str]:
    """
    Takes a repo name like "gocodeup/codeup-setup-script" and returns a
    dictionary with the language of the repo and the readme contents.
    """
    contents = get_repo_contents(repo)
    readme_download_url = get_readme_download_url(contents)
    if readme_download_url == "":
        readme_contents = None
    else:
        readme_contents = requests.get(readme_download_url).text
    return {
        "repo": repo,
        "language": get_repo_language(repo),
        "readme_contents": readme_contents,
    }


def scrape_github_data() -> List[Dict[str, str]]:
    """
    Loop through all of the repos and process them. Returns the processed data.
    """
    return [process_repo(repo) for repo in REPOS]


if __name__ == "__main__":
    data = scrape_github_data()
    json.dump(data, open("data.json", "w"), indent=1)


print('git acquire module loaded successsfully')