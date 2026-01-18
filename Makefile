

build_tool:
	buf generate --template buf.gen.yaml . --path ./src/proto/tool/tool.proto

build_api:
	buf generate --template buf.gen.yaml . --path ./src/proto/api/api.proto

build_all:
	buf generate --template buf.gen.yaml .