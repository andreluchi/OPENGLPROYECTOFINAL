vertex_shader = """
#version 450
layout (location = 0) in vec3 position;
layout (location = 1) in vec3 normal;
layout (location = 2) in vec2 texCoords;

uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;

uniform float tiempo;
uniform float valor;
uniform vec3 pointLight;
out float intensity;
out vec3 outColor;
out vec2 outTexCoords;

void main()
{
    vec4 norm = vec4(normal, 0.0);

    vec4 pos = vec4(position, 1.0) + norm * valor;
    pos = modelMatrix * pos;

    vec4 light = vec4(pointLight, 1.0);

    intensity = dot(modelMatrix * norm, normalize(light - pos));

    gl_Position = projectionMatrix * viewMatrix * pos;

    outColor = vec3(3.0,2.0 - valor * 2,1.0-valor * 1) * 0.5*intensity;
    outTexCoords = texCoords;
}
"""


fragment_shader = """
#version 450
layout (location = 0) out vec4 fragColor;

in vec3 outColor;
in vec2 outTexCoords;

uniform sampler2D tex;

void main()
{
    fragColor = vec4(outColor, 1) * texture(tex, outTexCoords);
}


"""
termico_shader="""
#version 450

layout (location = 0) out vec4 fragColor;

in float intensity;
void main()
{
  vec4 color;
	if (intensity > 0.6)
		color = vec4(1.0,0,0,0);
	else if (intensity > 0.2)
		color = vec4(0,1.0,0,0);
	else
		color = vec4(0,0,1.0,0);
	fragColor = color;

}

"""

ocean_shader="""
#version 450

layout (location = 0) out vec4 fragColor;

in float intensity;
void main()
{
  vec4 color;
  color= vec4(intensity,intensity,1,0);
	fragColor = color;

}

"""

radioactivo_shader="""
#version 450

layout (location = 0) out vec4 fragColor;

in float intensity;
void main()
{
  vec4 color;
  color= vec4(1-intensity,1,1-intensity,0);
	fragColor = color;

}

"""

whiteout_shader = """
#version 450
layout (location = 0) out vec4 fragColor;
in vec3 outColor;
in vec2 outTexCoords;
uniform sampler2D tex;
void main()
{
    fragColor = vec4(2, 5, 6, 9);
}
""" 
Blackwhite_shader = """
#version 450
layout (location = 0) out vec4 fragColor;
in vec3 outColor;
in vec2 outTexCoords;
uniform vec3 pointLight;
uniform sampler2D tex;
void main()
{
    fragColor = vec4(outColor, 1) * texture(tex, outTexCoords);
    float color = (fragColor.x + fragColor.y + fragColor.z) / 3.0;
    fragColor = vec4(color, color, color, 1);
}
"""

start_shader = """
#version 450
layout (location = 0) out vec4 fragColor;
in vec3 outColor;
in vec2 outTexCoords;
uniform sampler2D tex;
void main()
{
    fragColor = vec4(outColor, 1) * texture(tex, outTexCoords);
}
"""

