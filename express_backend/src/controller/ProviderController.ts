import { Router, Response, Request } from "express";
import { z } from "zod";
import { PrismaClient } from "@prisma/client";
import { Code, sendTemplate } from "../model/template";
const prisma = new PrismaClient();
const router: Router = Router();

// get all stuff
router.get("", async (req: Request, res: Response) => {});

router.get("/:email", async (req: Request, res: Response) => {
  const idParamScheme = z.number({ required_error: "email Param Required" });
  const valid = idParamScheme.safeParse(Number(req.params.email));
  if (!valid.success) return res.status(400).send(valid);

  const email = req.params.email;
  const getProviderAvail = await prisma.provider_Availability.findUnique({
    where: {
      email: email,
    },
  });
});
// post something
router.post("/", async (req: Request, res: Response) => {
  const bodyScheme = z.object({
    email: z.string().email(),
    mon: z.boolean(),
    tue: z.boolean(),
    wed: z.boolean(),
    thu: z.boolean(),
    fri: z.boolean(),
    sat: z.boolean(),
    sun: z.boolean(),
  });

  const valid = bodyScheme.safeParse(req.body);
  if (!valid.success) res.status(400).send(valid);

  type IBody = z.infer<typeof bodyScheme>;
  const body: IBody = req.body;

  const editProviderAvail = await prisma.provider_Availability
    .create({
      data: {
        email: body.email,
        mon: body.mon,
        tue: body.tue,
        wed: body.wed,
        thu: body.thu,
        fri: body.fri,
        sat: body.sat,
        sun: body.sun,
      },
    })
    .then(() => {
      console.log("success on creating provider_Availability");
    });
});

// update something
router.put("/:id", async (req: Request, res: Response) => {
  const bodySchema = z.object({
    email: z.string().email(),
    mon: z.boolean(),
    tue: z.boolean(),
    wed: z.boolean(),
    thu: z.boolean(),
    fri: z.boolean(),
    sat: z.boolean(),
    sun: z.boolean(),
  });

  const valid = bodySchema.safeParse(req.body);
  if (!valid.success) res.status(400).send(valid);

  type IBody = z.infer<typeof bodySchema>;
  const body: IBody = req.body;

  await prisma.provider_Availability.update({
    where: {
      email: body.email,
    },
    data: {
      mon: body.mon,
      tue: body.tue,
      wed: body.wed,
      thu: body.thu,
      fri: body.fri,
      sat: body.sat,
      sun: body.sun,
    },
  });
});
// delete specific record
router.delete("/:id", async (req: Request, res: Response) => {
  const paramSchema = z.number();
  const valid = paramSchema.safeParse(Number(req.params.id));
  if (!valid.success) return res.status(Code.S400_Bad_Request).send(valid);

  const userid = res.locals.userid;
});

export const ProviderAvailController: Router = router;
