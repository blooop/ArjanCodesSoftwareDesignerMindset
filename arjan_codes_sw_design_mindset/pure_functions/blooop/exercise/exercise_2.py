from dataclasses import dataclass


@dataclass
class Laptop:
    machine_name: str = "DULL"

    def install_os(self) -> None:
        print("Installing OS")

    def format_hd(self) -> None:
        print("Formatting the hard drive")

    def create_admin_user(self, password: str) -> None:
        print(f"Creating admin user with password {password}.")

    def factory_reset(self):
        self.format_hd()
        self.machine_name = "DULL"
        self.install_os()
        self.create_admin_user("admin")


def factory_reset(laptop: Laptop):
    laptop.format_hd()
    laptop.machine_name = "DULL"
    laptop.install_os()
    laptop.create_admin_user("admin")
    return laptop


def main() -> None:
    laptop = Laptop()
    laptop.factory_reset()
    print(laptop)

    laptop2 = factory_reset(Laptop())

    print(laptop2)


if __name__ == "__main__":
    main()
