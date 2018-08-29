import docker
import os

docker_client = docker.DockerClient()

tag = 'my-hello-world'
context = os.path.abspath('.')
dockerfile = os.path.abspath(os.path.join(os.path.join('folder', 'folder', 'Dockerfile')))

print('Tag: {0}'.format(tag))
print('Context path: {0}'.format(context))
print('Dockerfile path: {0}'.format(dockerfile))

# This does not work
docker_client.images.build(tag=tag, path=context, dockerfile=dockerfile)

print()
print('A work around which works')

dockerfile_rel = os.path.relpath(dockerfile, context)
dockerfile_rel = dockerfile_rel.replace('\\', '/')

print('Tag: {0}'.format(tag))
print('Context path: {0}'.format(context))
print('Dockerfile path: {0}'.format(dockerfile_rel))

res = docker_client.images.build(tag=tag, path=context, dockerfile=dockerfile_rel)
print('Successfully built image: {0}'.format(res))
