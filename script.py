from envyaml import EnvYAML
import pyaml

# ベースとなるYAML設定ファイルに環境毎の値を反映して出力する
def main():
    # 全体を設定ファイルとして使いたいので環境変数を含めない
    rendered = EnvYAML(yaml_file='common.yaml', include_environment=False)

    # いい感じにフォーマットして出力する
    print(pyaml.dump(rendered.export()))

if __name__ == '__main__':
    main()
