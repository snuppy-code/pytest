{
  description = "devshell for developing this game";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-26.05";
    nixgl.url = "github:nix-community/nixGL";
    nixgl.inputs.nixpkgs.follows = "nixpkgs";
  };

  outputs = {
    self,
    nixpkgs,
    nixgl,
  }: let
    system = "x86_64-linux";
    pkgs = import nixpkgs {
      inherit system;
      overlays = [nixgl.overlay];
    };
  in {
    devShells.${system}.default = pkgs.mkShell {
      packages = [
        pkgs.nixgl.nixGLIntel
        (pkgs.python314.withPackages (ps: with ps; [pygame-ce]))
      ];
      shellHook = ''
        echo "Entered Nix devShell."
        echo "Use 'nixGLIntel <command>' to run with hardware acceleration. (Should also fix issues with running on non-nixos systems.)"

        alias npy="nixGLIntel python -m "

        echo "Aliased: \`npy=\"nixGLIntel python -m \"\` (supply module path, e.g. \`npy src.main\`)"
      '';
    };
  };
}
